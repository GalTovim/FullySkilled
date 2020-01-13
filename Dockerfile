# build
FROM node:11.12.0-alpine as build-vue
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend .
RUN npm run build

# production
FROM nginx:stable-alpine as production
WORKDIR /app
RUN apk update && apk add --no-cache python3 make g++ cmake && \
      python3 -m ensurepip && \
      rm -r /usr/lib/python*/ensurepip && \
      pip3 install --upgrade pip setuptools wheel && \
      if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
      if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
      rm -r /root/.cache
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY --from=build-vue /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./backend/requirements.txt ./
RUN apk update \
      && apk add --virtual build-deps gcc python3-dev musl-dev \
      && apk add postgresql \
      && apk add postgresql-dev \
      && pip install psycopg2 \
      && apk add jpeg-dev zlib-dev libjpeg \
      && pip install Pillow \
      && apk del build-deps
RUN pip install dlib
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY ./backend .
CMD gunicorn -b 0.0.0.0:5000 app:app --daemon && \
      sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
      nginx -g 'daemon off;'
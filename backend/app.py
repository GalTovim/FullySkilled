from collections import OrderedDict

from flask import Flask, jsonify, flash, request, redirect
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from werkzeug.utils import secure_filename
import face_recognition
from mongoengine.errors import NotUniqueError, DoesNotExist

from models import *


app = Flask(__name__)
CORS(app)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MONGODB_HOST'] = 'mongodb+srv://tar:FullySkilled@cluster0-byfy8.mongodb.net/FullySkilled?retryWrites=true' \
                             '&w=majority'

db = MongoEngine(app)


@app.route('/api/register', methods=['POST'])
def register():
    content = request.form
    user = User(username=content['username'],
                password=content['password'],
                role=content['role'],
                firstname=content['firstname'],
                lastname=content['lastname'],
                email=content['email'],
                phone=content['phone'],
                idnum=content['idnum'])
    if content['role'] == 'Employee':
        user.city = content['city']
        user.street = content['street']
        user.apartment = content['apartment']
    if 'photo' in request.files:
        unknown_image = face_recognition.load_image_file(
            request.files['photo'])
        try:
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[
                0]
        except IndexError:
            return jsonify({'status': '400', 'error': 'No face in image'})

        user.photo = request.files['photo']
    try:
        user.save()
    except NotUniqueError:
        return jsonify({'status': 400, 'error': 'User with username ' + content['username'] + ' already exists'})

    return jsonify({'status': 200, 'message': 'User registered successfully', 'user': user})


@app.route('/api/login', methods=['POST'])
def login():
    content = request.form
    if 'photo' in request.files:
        unknown_image = face_recognition.load_image_file(
            request.files['photo'])
        try:
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[
                0]
        except IndexError:
            return jsonify({'status': '400', 'error': 'No face in image'})

        known_faces = OrderedDict()
        for user in User.objects():
            known_faces[user.username] = face_recognition.face_encodings(
                face_recognition.load_image_file(user.photo))[0]

        results = face_recognition.compare_faces(
            list(known_faces.values()), unknown_face_encoding)
        if True not in results:
            return jsonify({'status': 404, 'error': 'Face not found'})
        else:
            index = [i for i, val in enumerate(results) if val][0]
            k = list(known_faces.keys())
            return jsonify({'status': 200, 'message': 'Face is {0}'.format(k[index]),
                            'user': User.objects.get(username=k[index])})
    else:
        try:
            user = User.objects.get(username=content['username'])
            if user.password == content['password']:
                return jsonify({'status': 200, 'message': 'logged in', 'user': user})
            else:
                return jsonify({'status': 404, 'error': 'Wrong password'})
        except DoesNotExist:
            return jsonify({'status': 404, 'error': 'Could not find user ' + content['username']})


@app.route('/api/addBusiness', methods=['POST'])
def add_business():
    content = request.form
    user = User.objects.get(username=content['owner'])
    if user.role != 'Employer':
        return jsonify({'status': 401, 'error': 'Only employers can add their business'})
    business = Business(name=content['businessname'], owner=user)
    if 'city' in content:
        business.city = content['city']
    if 'street' in content:
        business.street = content['street']
    if 'apartment' in content:
        business.apartment = content['apartment']
    business.save()

    # except NotUniqueError:
    #     return jsonify({'status': 400, 'error': 'Business name already exists'})
    return jsonify({'status': 200, 'message': 'Business added successfully'})


@app.route('/api/addJob', methods=['POST'])
def add_job():
    content = request.form
    business = Business.objects.get(name=content['businessname'])
    if business.owner.username != content['username']:
        return jsonify({'status': 401, 'error': 'You can only add a job to your business'})
    job = Job(title=content['title'],
              business=business.name, address='{0} {1} {2}'.format(business.city,business.street, business.apartment))
    if 'description' in content:
        job.description = content['description']
    try:
        business.update(add_to_set__jobs=job)
    except NotUniqueError:
        return jsonify({'status': 400, 'error': 'Job with this title exists'})
    return jsonify({'status': 200, 'message': 'Job added'})


@app.route('/api/getBusinesses/<username>', methods=['GET'])
def get_businesses(username):
    try:
        user = User.objects.get(username=username)
    except DoesNotExist:
        return jsonify({'status': 404, 'error': 'User does not exist'})
    businesses = Business.objects.get(owner=user)
    return jsonify({'status': 200, 'businesses': businesses.to_json()})


@app.route('/api/applyJob', methods=['POST'])
def apply_job():
    content = request.form
    business = Business.objects.get(name=content['businessname'])
    job = business.jobs.filter(title=content['title'])[0]
    job.applicants.append(content['username'])
    business.save()
    return jsonify({'status': 200, 'message': 'Applied for job'})


@app.route('/api/addQuestion', methods=['POST'])
def add_question():
    content = request.form
    count = Faq.objects.count()
    count += 1
    faq = Faq(question=content['question'],
              answer=content['answer'], number=count)
    faq.save()
    return jsonify({'status': 200, 'message': 'Question added'})


@app.route('/api/getQuestions', methods=['GET'])
def get_questions():
    questions = Faq.objects()
    return jsonify({'status': 200, 'questions': questions})


@app.route('/api/admin/getBusinesses', methods=['GET'])
def admin_get_businesses():
    businesses = Business.objects()
    return jsonify({'status': 200, 'businesses': businesses})


@app.route('/api/admin/getEmployees', methods=['GET'])
def admin_get_employees():
    users = User.objects.filter(role="Employee")
    return jsonify({'status': 200, 'users': users})


@app.route('/api/admin/getEmployers', methods=['GET'])
def admin_get_employers():
    users = User.objects.filter(role="Employer")
    return jsonify({'status': 200, 'users': users})


@app.route('/api/getJobs', methods=['GET'])
def get_jobs():
    jobs = Business.objects.distinct(field='jobs')
    return jsonify({'jobs': jobs})


@app.route('/api/admin', methods=['GET'])
def admin():
    users = User.objects.count()
    businesses = Business.objects.count()
    faqs = Faq.objects.count()
    jobs = len(Business.objects.distinct(field='jobs'))
    return jsonify({'users': users, 'businesses': businesses, 'faqs': faqs, 'jobs': jobs})


if __name__ == '__main__':
    app.run()

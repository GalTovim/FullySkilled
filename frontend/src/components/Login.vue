<template>
  <div id="login">
    <h1>Login</h1>
    <input type="text" name="username" v-model="input.username" placeholder="Username" />
    <input type="password" name="password" v-model="input.password" placeholder="Password" />
    <button type="button" @click="login()">Login</button>
    <button type="button" @click="flipCamera">Face Login</button>
    <Webcam v-if="camera === true" @capture="oncapturechild" />
  </div>
</template>

<script>
import axios from "axios";
import Webcam from "./Webcam";

export default {
  name: "login",
  components: { Webcam },
  data() {
    return {
      input: {
        username: "",
        password: ""
      },
      response: "",
      image: null,
      camera: false
    };
  },
  methods: {
    login() {
      const path = "http://localhost:5000/api/login";

      if ((this.input.username && this.input.password) || this.image) {
        const formData = new FormData();
        formData.append("username", this.input.username);
        formData.append("password", this.input.password);
        if (this.image) formData.append("photo", this.image, "user.jpeg");

        axios
          .post(path, formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(res => {
            console.log(res);
          });
      }
    },
    flipCamera() {
      this.camera = !this.camera;
    },
    dataURItoBlob(dataURI, type) {
      // convert base64 to raw binary data held in a string
      var byteString = atob(dataURI.split(",")[1]);

      // separate out the mime component
      var mimeString = dataURI
        .split(",")[0]
        .split(":")[1]
        .split(";")[0];

      // write the bytes of the string to an ArrayBuffer
      var ab = new ArrayBuffer(byteString.length);
      var ia = new Uint8Array(ab);
      for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }

      // write the ArrayBuffer to a blob, and you're done
      var bb = new Blob([ab], { type: type });
      return bb;
    },
    oncapturechild(img) {
      this.image = this.dataURItoBlob(img, "image/jpeg");
    }
  }
};
</script>

<style scoped></style>

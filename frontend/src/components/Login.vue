<template>
  <div id="login">
    <h1>Login</h1>
    <b-container>
      <b-form-input type="text" name="username" v-model="input.username" placeholder="Username" />
      <b-form-input
        type="password"
        name="password"
        v-model="input.password"
        placeholder="Password"
      />
      <b-button type="button" @click="flipCamera">Face Login</b-button>
      <b-button type="button" variant="success" @click="login()">Login</b-button>
    </b-container>

    <b-alert
      v-model="alert.showDismissibleAlert"
      variant="danger"
      dismissible
    >{{alert.alertContent}}</b-alert>
    <Webcam v-if="camera === true" @capture="oncapturechild" />
  </div>
</template>

<script>
import axios from "axios";
import Webcam from "./Webcam";

import router from "../router";
import store from "../store";

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
      camera: false,
      alert: {
        showDismissibleAlert: false,
        alertContent: ""
      }
    };
  },
  methods: {
    login() {
      const path = "/api/login";

      if ((this.input.username && this.input.password) || this.image) {
        const formData = new FormData();
        if (this.image) formData.append("photo", this.image, "user.jpeg");
        else {
          formData.append("username", this.input.username);
          formData.append("password", this.input.password);
        }

        axios
          .post(path, formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(res => {
            console.log(res);
            if (res.data.error) {
              this.alert.alertContent = res.data.error;
              this.alert.showDismissibleAlert = true;
            } else {
              const role = res.data.user.role;
              store.commit("updateUser", res.data.user);
              if (role === "Admin") router.push({ name: "admin" });
              else if (role === "Employer")
                router.push({
                  name: "employer"
                });
              else if (role === "Employee")
                router.push({
                  name: "employee"
                });
            }
          })
          .catch(err => console.log(err));
      }
    },
    flipCamera() {
      this.camera = !this.camera;
      this.image = null;
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

<style scoped lang="scss"></style>

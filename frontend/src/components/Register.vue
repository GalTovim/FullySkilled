<template>
  <div id="register">
    <h1>Register</h1>
    <input type="text" name="username" v-model="input.username" placeholder="Username" />
    <input type="password" name="password" v-model="input.password" placeholder="Password" />
    <select name="roles" v-model="input.role">
      <option value="Employee">Employee</option>
      <option value="Employer">Employer</option>
    </select>
    <button type="button" @click="flipCamera">Upload Image</button>
    <button type="button" @click="register()">Register</button>
    <Webcam v-if="camera === true" @capture="oncapturechild" />
  </div>
</template>

<script>
import axios from "axios";
import Webcam from "./Webcam";

export default {
  name: "register",
  components: { Webcam },
  data() {
    return {
      input: {
        username: "",
        password: "",
        role: ""
      },
      response: "",
      camera: false,
      image: null
    };
  },
  methods: {
    register() {
      const path = "http://localhost:5000/api/register";
      const formData = new FormData();
      if (this.input.username && this.input.password && this.input.role) {
        formData.append("username", this.input.username);
        formData.append("password", this.input.password);
        formData.append("role", this.input.role);
        if (this.image) formData.append("photo", this.image, "user.jpeg");

        axios
          .post(path, formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(res => console.log(res))
          .catch(err => console.log(err));
      }
    },
    flipCamera() {
      this.camera = !this.camera;
    },
    oncapturechild(img) {
      this.image = img;
    },
    getRole(role) {
      this.input.role = role;
    }
  }
};
</script>

<style scoped></style>

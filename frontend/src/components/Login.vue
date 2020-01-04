<template>
  <div id="login">
    <h1>Login</h1>
    <input
      type="text"
      name="username"
      v-model="input.username"
      placeholder="Username"
    />
    <input
      type="password"
      name="password"
      v-model="input.password"
      placeholder="Password"
    />
    <button type="button" @click="login()">Login</button>
    <button type="button">Face Login</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "login",
  data() {
    return {
      input: {
        username: "",
        password: ""
      },
      response: ""
    };
  },
  methods: {
    login() {
      const path = "http://localhost:5000/api/login";

      if (this.input.username && this.input.password) {
        const formData = new FormData();
        formData.append("username", this.input.username);
        formData.append("password", this.input.password);

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
    }
  }
};
</script>

<style scoped></style>

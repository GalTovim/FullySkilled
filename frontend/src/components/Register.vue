<template>
  <div id="login">
    <h1>Register</h1>
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
    <button type="button" @click="register()">Register</button>
    <button type="button">Upload Photo</button>
  </div>
</template>

<script>
//import axios from "axios";

export default {
  name: "register",
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
    register() {
      //const path = "http://localhost:5000/api/register";
    }
  }
};
</script>

<style scoped></style>

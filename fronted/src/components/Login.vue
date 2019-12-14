<template>
<<<<<<< HEAD
<h1>
yehudaa is the only leader
</h1>
 </template>>
=======
  <div class="login">
    <div v-if="loggingIn" class="container-loading">
      <img src="/loading.gif" alt="Loading Icon" />
    </div>
    <p v-if="loginError">{{ loginError }}</p>
    <p v-if="loginSuccessful">Login Successful</p>
    <form @submit.prevent="loginSubmit">
      <input type="text" placeholder="Username" v-model="username" />
      <input type="password" placeholder="Password" v-model="password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>
>>>>>>> a88714b1ef5c91f157df35ff700fa539f66294f0

<script>
import axios from "axios";

export default {
  name: "Login",
  data: () => {
    return {
      loginError: false,
      loginSucccessfful: false
    };
  },
  methods: {
    loginSubmit: function(submitEvent) {
      axios
        .post("localhost:4000/login", {
          username: submitEvent.username,
          password: submitEvent.password
        })
        .then(res => {
          if (res.status == 200) this.loginSucccessfful = true;
        })
        .catch(err => (this.loginError = err.message));
    }
  }
};
</script>
>

<style scoped lang="scss">
.login {
  border: 1px solid black;
  border-radius: 5px;
  padding: 1.5rem;
  width: 300px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
  overflow: hidden;
  .container-loading {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.3);
    img {
      width: 2rem;
      height: 2rem;
    }
  }
  form {
    display: flex;
    flex-flow: column;
    *:not(:last-child) {
      margin-bottom: 1rem;
    }
    input {
      padding: 0.5rem;
    }
    button {
      padding: 0.5rem;
      background-color: lightgray;
      border: 1px solid gray;
      border-radius: 3px;
      cursor: pointer;
      &:hover {
        background-color: lightslategray;
      }
    }
  }
}
</style>

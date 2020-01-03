<template>
  <div class="home">
    <div v-if="this.hasAccount === false">
      <Register />
      <button @click="flipHasAccount()">I have an account</button>
    </div>
    <div v-else>
      <Login />
      <button @click="flipHasAccount()">I don't have an account</button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";

export default {
  name: "home",
  components: {
    Register,
    Login
  },
  data() {
    return {
      hasAccount: false
    };
  },
  methods: {
    flipHasAccount() {
      this.hasAccount = !this.hasAccount;
    }
  }
};
</script>

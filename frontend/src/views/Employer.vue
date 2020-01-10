<template>
  <div>
    <Navbar role="employer" />
    <h1>Welcome {{user.username}}</h1>
  </div>
</template>

<script>
import Navbar from "../components/Nav";

export default {
  name: "employer",
  components: { Navbar },
  props: ["user"],
  data() {
    return {
      input: {
        bussinessname: "",
        bussinessaddress: ""
      }
    };
  },
  methods() {}
};
</script>

<style scoped>
</style>
<template>
  <div>
    <Navbar role="employer" />
    <h1>Welcome {{this.user.username}}</h1>
  </div>
</template>

<script>
import Navbar from "../components/Nav";
import { mapState } from "vuex";

export default {
  name: "employer",
  components: { Navbar },
  computed: {
    ...mapState(["user"])
  },
  data() {
    return {
      input: {
        bussinessname: "",
        bussinessaddress: ""
      }
    };
  },
  methods: {}
};
</script>

<style scoped>
</style>
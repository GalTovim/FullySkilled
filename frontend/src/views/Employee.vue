<template>
  <div>
    <Navbar role="employee" />
    <h1>Welcome {{this.user.username}}</h1>
  </div>
</template>

<script>
import Navbar from "../components/Nav";
import { mapState } from "vuex";

export default {
  name: "employee",
  components: { Navbar },
  computed: {
    ...mapState(["user"])
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style scoped>
</style>
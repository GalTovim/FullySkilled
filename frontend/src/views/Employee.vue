<template>
  <div>
    <Navbar role="employee" />
    <h1>Welcome {{user.username}}</h1>
  </div>
</template>

<script>
import Navbar from "../components/Nav";

export default {
  name: "employee",
  components: { Navbar },
  props: ["user"],
  data() {
    return {};
  },
  methods: {}
};
</script>

<style scoped>
</style>
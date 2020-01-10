<template>
  <div>
    <Navbar role="admin" />
  </div>
</template>

<script>
import Navbar from "../components/Nav";
export default {
  name: "admin",
  components: { Navbar },
  data() {
    return {
      items: []
    };
  },
  methods: {}
};
</script>

<style scoped>
</style>
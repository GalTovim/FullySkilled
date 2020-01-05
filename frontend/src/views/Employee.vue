<template>
  <div>
    <h1>Welcome {{user.username}}</h1>
  </div>
</template>

<script>
export default {
  name: "employee",
  props: ["user"],
  data() {
    return {};
  },
  methods: {}
};
</script>

<style scoped>
</style>
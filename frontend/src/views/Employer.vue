<template>
  <div>
    <h1>Welcome {{user.username}}</h1>
  </div>
</template>

<script>
export default {
  name: "employer",
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
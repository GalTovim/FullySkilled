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
        bussinessaddress: "",
        office: "", //anaf misra
        typejob: "",
      }
    };
  },
  methods() {}
};
</script>

<style scoped>
</style>
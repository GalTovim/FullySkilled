<template>
  <div>
    <Navbar role="admin" />
  </div>
</template>

<script>
import Navbar from "../components/Nav";
import { mapState } from "vuex";

export default {
  name: "admin",
  components: { Navbar },
  computed: {
    ...mapState(["user"])
  },
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
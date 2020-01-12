<template>
  <div>
    <Navbar role="admin" />
    <h1>System Report</h1>
    <b-list-group>
      <b-list-group-item v-for="(value, key) in items" :key="key.id">Number of {{key}}: {{value}}</b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import Navbar from "../components/Nav";
import { mapState } from "vuex";
import axios from "axios";

export default {
  name: "admin",
  components: { Navbar },
  computed: {
    ...mapState(["user"])
  },
  data() {
    return {
      items: {}
    };
  },
  beforeMount() {
    const path = "/api/admin";

    axios
      .get(path)
      .then(res => {
        console.log(res);
        this.items = res.data;
      })
      .catch(err => console.log(err));
  },
  methods: {}
};
</script>

<style scoped>
</style>
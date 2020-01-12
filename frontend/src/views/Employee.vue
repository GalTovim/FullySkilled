<template>
  <div>
    <Navbar role="employee" />
    <h1>Here are jobs for you {{this.user.username}}</h1>
    <JobItem
      v-for="job in jobs"
      :key="job.id"
      :title="job.title"
      :business="job.business"
      :description="job.description"
      :location="job.address"
    />
  </div>
</template>

<script>
import Navbar from "../components/Nav";
import JobItem from "../components/JobItem";
import { mapState } from "vuex";

import axios from "axios";

export default {
  name: "employee",
  components: { Navbar, JobItem },
  computed: {
    ...mapState(["user"])
  },
  data() {
    return {
      jobs: []
    };
  },
  beforeMount() {
    const path = "/api/getJobs";

    axios.get(path).then(res => {
      this.jobs = res.data.jobs;
    });
  },
  methods: {}
};
</script>

<style scoped>
</style>
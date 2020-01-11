<template>
  <div>
    <b-card :title="title">
      <ul>
        <li>
          <b-card-text>Employer: {{business}}</b-card-text>
        </li>
        <li>
          <b-card-text>Job description: {{description}}</b-card-text>
        </li>
        <li>
          <b-card-text>Located in: {{location}}</b-card-text>
        </li>
      </ul>
      <b-alert variant="success" dismissible v-model="show">Applied to job</b-alert>

      <b-button @click="apply">Apply</b-button>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "JobItem",
  props: ["title", "description", "business", "location"],
  computed: {
    ...mapState(["user"])
  },
  data() {
    return { show: false };
  },
  methods: {
    apply() {
      const path = "http://localhost:5000/api/applyJob";
      const formData = new FormData();

      formData.append("businessname", this.business);
      formData.append("title", this.title);
      formData.append("username", this.user.username);

      axios
        .post(path, formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(res => {
          console.log(res);
          this.show = true;
        });
    }
  }
};
</script>

<style>
</style>
<template>
  <div>
    <b-card :title="title">
      <b-list-group>
        <b-list-group-item>
          <b-card-text>Employer: {{business}}</b-card-text>
        </b-list-group-item>
        <b-list-group-item>
          <b-card-text>Job description: {{description}}</b-card-text>
        </b-list-group-item>
        <b-list-group-item>
          <b-card-text>Located in: {{location}}</b-card-text>
        </b-list-group-item>
      </b-list-group>
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
      const path = "/api/applyJob";
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
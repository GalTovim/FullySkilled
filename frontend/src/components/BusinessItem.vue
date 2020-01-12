<template>
  <div>
    <b-card :title="name">
      <b-list-group>
        <b-list-group-item>Address: {{apartment}} {{street}}, {{city}}</b-list-group-item>
        <b-list-group-item>Jobs:</b-list-group-item>
        <b-list-group-item v-for="job in jobs" :key="job.id">
          {{job.title}}: {{job.description}}
          <b-list-group>
            <b-list-group-item>Applicants:</b-list-group-item>
            <b-list-group-item v-for="item in job.applicants" :key="item.id">{{item}}</b-list-group-item>
          </b-list-group>
        </b-list-group-item>
      </b-list-group>
      <b-button @click="showForm = !showForm">Add Job</b-button>
      <b-form-group v-if="showForm">
        <b-form-input v-model="title" placeholder="Title"></b-form-input>
        <b-form-input v-model="description" placeholder="Description"></b-form-input>
        <b-button @click="submitJob">Submit</b-button>
      </b-form-group>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "BusinessItem",
  props: ["name", "city", "street", "apartment", "jobs"],
  computed: {
    ...mapState(["user"])
  },
  data() {
    return { showForm: false, title: "", description: "" };
  },
  methods: {
    addJob() {},
    submitJob() {
      const path = "http://localhost:5000/api/addJob";

      const formData = new FormData();
      formData.append("username", this.user.username);
      formData.append("businessname", this.name);
      formData.append("title", this.title);
      formData.append("description", this.description);

      axios
        .post(path, formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(res => console.log(res));
    }
  }
};
</script>

<style>
</style>
<template>
  <div>
    <b-card :title="name">
      <b-list-group>
        <b-list-group-item>Address: {{apartment}} {{street}}, {{city}}</b-list-group-item>
        <b-list-group-item>Jobs:</b-list-group-item>
        <b-list-group-item v-for="job in jobs" :key="job.id">
          {{job.title}}: {{job.description}}
          <ul>
            <li v-for="item in job.applicants" :key="item.id">{{item}}</li>
          </ul>
        </b-list-group-item>
      </b-list-group>
      <b-button @click="addJob">Add Job</b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "BusinessItem",
  props: ["name", "city", "street", "apartment", "jobs"],
  data() {
    return {};
  },
  methods: { addJob() {} }
};
</script>

<style>
</style>
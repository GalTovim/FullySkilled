<template>
  <div>
    <b-card :title="title">
      <ul>
        <li>
          <b-card-text>Employer: {{business}}</b-card-text>
        </li>
        <li>
          <b-card-text>{{description}}</b-card-text>
        </li>
        <li>
          <b-card-text>Located in: {{location}}</b-card-text>
        </li>
      </ul>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "JobItem",
  props: ["title", "description", "business", "location"]
};
</script>

<style>
</style>
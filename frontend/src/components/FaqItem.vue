<template>
  <div>
    <b-card v-bind:title="question">
      <b-card-text>{{answer}}</b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "faq-item",
  props: ["question", "answer"]
};
</script>

<style>
</style>
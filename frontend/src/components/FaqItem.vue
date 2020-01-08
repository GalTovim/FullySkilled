<template>
  <div>
    <b-card v-bind:title="question">{{answer}}</b-card>
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
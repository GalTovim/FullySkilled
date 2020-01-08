<template>
  <div>
    <ul class="questions-list">
      <li v-for="faq in faqs" v-bind:key="faq.id">
        <Faqitem question="faq.quetion" answer="faq.answer" />
      </li>
    </ul>
  </div>
</template>

<script>
import Faqitem from "../components/FaqItem";
import axios from "axios";
export default {
  name: "faq",
  components: { Faqitem },
  data() {
    return {};
  },
  beforeMount() {
    const path = "http://localhost:5000/api/getQuestions";

    axios.get(path).then(res => {
      questions;
    });
  }
};
</script>


<style>
</style>
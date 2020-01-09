<template>
  <div>
    <ul class="questions-list">
      <b-card-group v-for="faq in faqs" v-bind:key="faq.id">
        <Faqitem v-bind:question="faq.question" v-bind:answer="faq.answer" />
      </b-card-group>

      <b-button v-b-modal.modal-prevent-closing>Add Question</b-button>
    </ul>

    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Enter question and answer"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <b-form-group
        :state="nameState"
        label="Name"
        label-for="name-input"
        invalid-feedback="Name is required"
      >
        <b-form-input id="name-input" v-model="name" :state="nameState" required></b-form-input>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
import Faqitem from "../components/FaqItem";
import axios from "axios";
export default {
  name: "faq",
  components: { Faqitem },
  data() {
    return { faqs: [] };
  },
  beforeMount() {
    const path = "http://localhost:5000/api/getQuestions";

    axios.get(path).then(res => {
      this.faqs = res.data.questions;
    });
  }
};
</script>

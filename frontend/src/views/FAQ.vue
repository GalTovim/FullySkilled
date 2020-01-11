<template>
  <div>
    <Navbar :role="user.role" />
    <b-list-group class="questions-list">
      <b-list-group-item href="#" v-for="faq in faqs" v-bind:key="faq.id">
        <Faqitem v-bind:question="faq.question" v-bind:answer="faq.answer" />
      </b-list-group-item>
      <b-button v-b-modal.modal-prevent-closing>Add Question</b-button>
    </b-list-group>

    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Enter question and answer"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          :state="questionState"
          label="Question"
          label-for="question-input"
          invalid-feedback="Question is required"
        >
          <b-form-input id="question-input" v-model="question" :state="questionState" required></b-form-input>
        </b-form-group>

        <b-form-group
          :state="answerState"
          label="Answer"
          label-for="answer-input"
          invalid-feedback="Answer is required"
        >
          <b-form-input id="answer-input" v-model="answer" :state="answerState" required></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script>
import Navbar from "../components/Nav";
import Faqitem from "../components/FaqItem";
import { mapState } from "vuex";

import axios from "axios";

export default {
  name: "faq",
  components: { Faqitem, Navbar },
  data() {
    return {
      faqs: [],
      question: "",
      answer: "",
      questionState: null,
      answerState: null
    };
  },
  methods: {
    resetModal() {
      this.question = "";
      this.answer = "";
      this.questionState = null;
      this.answerState = null;
    },
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.questionState = valid ? "valid" : "invalid";
      this.answerState = valid ? "valid" : "invalid";
      return valid;
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }

      const path = "http://localhost:5000/api/addQuestion";

      const formData = new FormData();
      formData.append("question", this.question);
      formData.append("answer", this.answer);

      axios.post(path, formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
      });
      this.$router.go();
    }
  },
  computed: {
    ...mapState(["user"])
  },
  beforeMount() {
    const path = "http://localhost:5000/api/getQuestions";

    axios.get(path).then(res => {
      this.faqs = res.data.questions;
    });
  }
};
</script>


<style>
</style>
<template>
  <div id="Employer">
    <Navbar role="employer" />
    <h1>Welcome {{user.username}}</h1>
    <BusinessItem
      v-for="business in businesses"
      :key="business.id"
      :name="business.name"
      :city="business.city"
      :street="business.street"
      :apartment="business.apartment"
      :jobs="business.jobs"
    />

    <b-modal
      v-if="showModal"
      id="modal-prevent-closing"
      ref="modal"
      title="Enter business details"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          :state="nameState"
          label="Name"
          label-for="name-input"
          invalid-feedback="Name is required"
        >
          <b-form-input id="name-input" v-model="name" :state="nameState" required></b-form-input>
        </b-form-group>

        <b-form-group
          :state="cityState"
          label="City"
          label-for="city-input"
          invalid-feedback="City is required"
        >
          <b-form-input id="city-input" v-model="city" :state="cityState" required></b-form-input>
        </b-form-group>

        <b-form-group
          :state="streetState"
          label="Street"
          label-for="street-input"
          invalid-feedback="Street is required"
        >
          <b-form-input id="street-input" v-model="street" :state="streetState" required></b-form-input>
        </b-form-group>

        <b-form-group
          :state="apartmentState"
          label="Apartment"
          label-for="apartment-input"
          invalid-feedback="Apartment is required"
        >
          <b-form-input id="apartment-input" v-model="apartment" :state="apartmentState" required></b-form-input>
        </b-form-group>
      </form>
    </b-modal>

    <b-button v-b-modal.modal-prevent-closing @click="showModal = true">Add Business</b-button>
  </div>
</template>

<script>
import axios from "axios";
import Navbar from "../components/Nav";
import { mapState } from "vuex";

import BusinessItem from "../components/BusinessItem";

export default {
  name: "employer",
  components: { Navbar, BusinessItem },
  computed: {
    ...mapState(["user"])
  },
  data() {
    return {
      businesses: [],
      nameState: null,
      cityState: null,
      streetState: null,
      apartmentState: null,
      name: "",
      city: "",
      apartment: "",
      street: "",
      showModal: false
    };
  },
  methods: {
    getBusinesses() {
      const path = "http://localhost:5000/api/getBusinesses/";

      axios.get(path + this.user.username).then(res => {
        console.log(res.data.businesses);
        this.businesses.push(...res.data.businesses);
      });
    },
    resetModal() {
      this.name = "";
      this.city = "";
      this.street = "";
      this.apartment = "";
      this.nameState = null;
      this.cityState = null;
      this.streetState = null;
      this.apartmentState = null;
    },
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
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

      const path = "http://localhost:5000/api/addBusiness";

      const formData = new FormData();
      formData.append("businessname", this.name);
      formData.append("city", this.city);
      formData.append("street", this.street);
      formData.append("apartment", this.apartment);
      formData.append("owner", this.user.username);

      axios
        .post(path, formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(res => console.log(res));
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
      });
      this.showModal = false;
      this.getBusinesses();
      // this.$router.go();
    }
  },

  beforeMount() {
    this.getBusinesses();
  }
};
</script>

<style scoped>
</style>
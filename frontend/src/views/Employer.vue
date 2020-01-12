<template>
  <div id="Employer">
    <h1>Welcome {{user.username}}</h1>
    <b-form-input type="text" name="bussinessname" v-model="input.bussinessname" placeholder="bussinessname" />
    <b-form-input type="text" name="address" v-model="input.address" placeholder="address" />
    <b-form-input type="text" name="office" v-model="input.office" placeholder="office" />
    <b-form-input type="text" name="typejob" v-model="input.typejob" placeholder="typejob" />
    <b-form-input type="text" name="salary" v-model="input.salary" placeholder="salary" />
    <b-button type="button" @click="add_business()">add_business</b-button>
  </div>
</template>

<script>
import axios from "axios";
import Navbar from "../components/Nav";
import { mapState } from "vuex";

export default {
  name: "employer",
  components: { Navbar },
  computed: {
    ...mapState(["user"])
  },
  data() {
    return {
      input: {
        bussinessname: "",
        address: "",
        office: "", //anaf misra
        typejob: "",
        salary: ""
      }
    };
  },
  methods: {
    add_business() {
        const path = "http://localhost:5000/api/addBussiness";

        if (this.input.bussinessname && this.input.bussinessaddress && this.input.office && this.input.typejob && this.input.salary )  {
            const formData = new FormData();
            formData.append("bussinessname", this.input.bussinessname);
            formData.append("address", this.input.address);
            formData.append("office", this.input.office);
            formData.append("typejob", this.input.typejob);
            formData.append("salary", this.input.salary);

            axios
            .post(path, formData, {
                headers: {
                "Content-Type": "multipart/form-data"
                }
            })
            .then(res => {
                if (res.data.error) {
                this.alert.alertContent = res.data.error;
                this.alert.showDismissibleAlert = true;
                }
            });
        }
        },
      
  }
};
</script>

<style scoped>
</style>
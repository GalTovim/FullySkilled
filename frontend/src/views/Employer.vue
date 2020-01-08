<template>
  <div>
    <h1>Welcome {{user.username}}</h1>
  </div>
</template>

<script>
export default {
  name: "employer",
  props: ["user"],
  data() {
    return {
      input: {
        bussinessname: "",
        bussinessaddress: "",
        office: "", //anaf misra
        typejob: "",
        salary: ""
      }
    };
  },
  methods: {
    addbussiness() {
        const path = "http://localhost:5000/api/Employer";

        if (this.input.bussinessname && this.input.bussinessaddress && this.input.office && this.input.typejob && this.input.salary )  {
            const formData = new FormData();
            formData.append("bussinessname", this.input.bussinessname);
            formData.append("bussinessaddress", this.input.bussinessaddress);
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
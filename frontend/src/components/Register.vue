<template>
  <div id="register">
    <h1>Register</h1>
    <b-form-input type="text" name="username" v-model="input.username" placeholder="Username" />
    <b-form-input type="password" name="password" v-model="input.password" placeholder="Password" />
    <b-form-input type="text" name="firstname" v-model="input.password" placeholder="First Name" />
    <b-form-input type="text" name="lastname" v-model="input.lastname" placeholder="Last Name" />
    <b-form-input type="email" name="email" v-model="input.email" placeholder="E-Mail" />
    <b-form-input type="text" name="phone" v-model="input.phone" placeholder="Phone" />

    <b-form-input
      v-if="input.role == 'Employee'"
      type="text"
      name="city"
      v-model="input.city"
      placeholder="City"
    />
    <b-form-input
      v-if="input.role == 'Employee'"
      type="text"
      name="street"
      placeholder="Street"
      v-model="input.street"
    />
    <b-form-input
      v-if="input.role == 'Employee'"
      type="text"
      name="apartment"
      placeholder="Apartment"
      v-model="input.apartment"
    />

    <b-form-select name="roles" v-model="input.role">
      <option value="Employee">Employee</option>
      <option value="Employer">Employer</option>
    </b-form-select>
    <b-button type="button" @click="flipCamera">Upload Image</b-button>
    <b-button type="button" variant="success" @click="register()">Register</b-button>
    <b-alert
      v-model="alert.showDismissibleAlert"
      variant="danger"
      dismissible
    >{{alert.alertContent}}</b-alert>
    <Webcam v-if="camera === true" @capture="oncapturechild" />
  </div>
</template>

<script>
import axios from "axios";
import Webcam from "./Webcam";
import router from "../router";
import store from "../store";

export default {
  name: "register",
  components: { Webcam },
  data() {
    return {
      input: {
        username: "",
        password: "",
        firstname: "",
        lastname: "",
        email: "",
        phone: "",
        role: "",
        city: "",
        street: "",
        apartment: ""
      },
      response: "",
      camera: false,
      image: null,
      alert: {
        showDismissibleAlert: false,
        alertContent: ""
      }
    };
  },
  methods: {
    register() {
      const path = "http://localhost:5000/api/register";
      const formData = new FormData();
      if (this.input.username && this.input.password && this.input.role) {
        formData.append("username", this.input.username);
        formData.append("password", this.input.password);
        formData.append("firstname", this.input.firstname);
        formData.append("lastname", this.input.lastname);
        formData.append("email", this.input.email);
        formData.append("phone", this.input.phone);
        formData.append("role", this.input.role);

        if (this.input.role === "Employee") {
          formData.append("city", this.input.city);
          formData.append("street", this.input.street);
          formData.append("apartment", this.input.apartment);
        }
        if (this.image) formData.append("photo", this.image, "user.jpeg");

        axios
          .post(path, formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(res => {
            console.log(res);
            if (res.data.error) {
              this.alert.alertContent = res.data.error;
              this.alert.showDismissibleAlert = true;
            } else {
              const role = res.data.user.role;
              store.commit("updateUser", res.data.user);
              if (role === "Admin") router.push({ name: "admin" });
              else if (role === "Employer")
                router.push({
                  name: "employer"
                });
              else if (role === "Employee")
                router.push({
                  name: "employee"
                });
            }
          })
          .catch(err => console.log(err));
      }
    },
    flipCamera() {
      this.camera = !this.camera;
    },
    dataURItoBlob(dataURI, type) {
      // convert base64 to raw binary data held in a string
      var byteString = atob(dataURI.split(",")[1]);

      // separate out the mime component
      var mimeString = dataURI
        .split(",")[0]
        .split(":")[1]
        .split(";")[0];

      // write the bytes of the string to an ArrayBuffer
      var ab = new ArrayBuffer(byteString.length);
      var ia = new Uint8Array(ab);
      for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }

      // write the ArrayBuffer to a blob, and you're done
      var bb = new Blob([ab], { type: type });
      return bb;
    },
    oncapturechild(img) {
      this.image = this.dataURItoBlob(img, "image/jpeg");
    },
    getRole(role) {
      this.input.role = role;
    }
  }
};
</script>

<style scoped lang="scss"></style>

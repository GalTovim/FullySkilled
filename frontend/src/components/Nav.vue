<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-brand>FullySkilled</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item :to="'/'+this.user.role">Home</b-nav-item>
        <b-nav-item to="/faq">FAQ</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Nav",
  computed: {
    ...mapState(["user"])
  }
};
</script>
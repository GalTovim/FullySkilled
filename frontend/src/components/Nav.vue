<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item :to="'/'+this.user.role">{{this.user.role}}</b-nav-item>
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
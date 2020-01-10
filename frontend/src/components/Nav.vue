<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item :href="'/'+this.user.role">Home</b-nav-item>
        <b-nav-item href="/faq">FAQ</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Nav",
  props: ["role"],
  computed: {
    ...mapState(["user"])
  }
};
</script>
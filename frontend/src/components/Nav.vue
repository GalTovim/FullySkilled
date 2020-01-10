<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item :href="'/'+this.role">Home</b-nav-item>
        <b-nav-item href="/faq">FAQ</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "Nav",
  props: ["role"]
};
</script>
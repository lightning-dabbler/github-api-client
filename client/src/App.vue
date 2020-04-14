<template>
  <div id="app">
    <nav-region emoji="octocat"></nav-region>
    <div class="container-fluid">
      <router-view></router-view>
    </div>
    <footer-region emoji="zap"></footer-region>
  </div>
</template>

<script>
console.info("module: App.vue");

import FooterRegion from "./components/app/FooterRegion.vue";
import NavRegion from "./components/app/NavRegion.vue";

export default {
  name: "app",
  components: {
    FooterRegion,
    NavRegion
  },
  data() {
    return {};
  }
};
</script>
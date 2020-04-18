<template>
  <div id="app">
    <nav-region emoji="octocat"></nav-region>
    <div class="container-fluid pb-5">
      <router-view></router-view>
    </div>
    <arrow-to-top></arrow-to-top>
    <footer-region emoji="zap"></footer-region>
  </div>
</template>

<script>
console.info("module: App.vue");

import FooterRegion from "./components/app/FooterRegion.vue";
import NavRegion from "./components/app/NavRegion.vue";
import ArrowToTop from './components/app/ArrowToTop.vue'

export default {
  name: "app",
  components: {
    FooterRegion,
    NavRegion,
    ArrowToTop
  },
  data() {
    return {};
  }
};
</script>
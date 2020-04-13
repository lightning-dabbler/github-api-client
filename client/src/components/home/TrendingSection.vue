<template>
  <section id="trending-section">
    <trending-header></trending-header>
    <trending-body></trending-body>
  </section>
</template>

<script>
console.info("module: TrendingSection.vue");
import TrendingBody from "./trending/TrendingBody.vue";
import TrendingHeader from "./trending/TrendingHeader.vue";
export default {
  name: "trending-section",
  components: { TrendingBody, TrendingHeader },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
</style>
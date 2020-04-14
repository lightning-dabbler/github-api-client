<template>
  <section id="trending-section">
    <trending-header></trending-header>
    <section class="container py-5">
      <section class="trending-rect">
      <trending-tabs class="py-3 px-3"></trending-tabs>
      <trending-refresh class="py-3"></trending-refresh>
      <trending-results></trending-results>
      </section>
    </section>
  </section>
</template>

<script>
console.info("module: TrendingSection.vue");
import TrendingResults from "./trending/TrendingResults.vue";
import TrendingTabs from "./trending/TrendingTabs.vue";
import TrendingHeader from "./trending/TrendingHeader.vue";
import TrendingRefresh from './trending/TrendingRefresh.vue'
export default {
  name: "trending-section",
  components: { TrendingResults, TrendingTabs, TrendingHeader, TrendingRefresh},
  data() {
    return {};
  }
};
</script>

<style lang="scss" scoped>
@import "@/static/css/custom.scss";

.trending-rect {
    background-color: transparent;
    border: 1px solid $ternary-color;
    border-radius: 3px;
}
</style>
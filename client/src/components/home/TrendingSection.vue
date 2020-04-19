<template>
  <section id="trending-section">
    <trending-header></trending-header>
    <section class="container py-5">
      <section class="trending-rect vld-parent">
        <vue-loading
          :active.sync="getTrendingLoader.active"
          :can-cancel="getTrendingLoader.canCancel"
          :is-full-page="getTrendingLoader.isFullPage"
          :color="getTrendingLoader.color"
          :loader="getTrendingLoader.loader"
          :width="getTrendingLoader.width"
          :height="getTrendingLoader.height"
          :background-color="getTrendingLoader.backgroundColor"
          :opacity="getTrendingLoader.opacity"
          :z-index="getTrendingLoader.zIndex"
        ></vue-loading>
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
import TrendingRefresh from "./trending/TrendingRefresh.vue";
import VueLoading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
const { mapGetters } = require("vuex");

export default {
  name: "trending-section",
  components: {
    TrendingResults,
    TrendingTabs,
    TrendingHeader,
    TrendingRefresh,
    VueLoading
  },
  computed: mapGetters(["getTrendingLoader"]),
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
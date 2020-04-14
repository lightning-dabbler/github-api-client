<template>
  <section id="trending-header">
    <header class="container gh-trend-header py-3 text-center">GitHub Trending</header>
  </section>
</template>
<script>
console.log("module: TrendingHeaders.vue");
export default {};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

#trending-header {
  background-color: $primary-color;
}
.gh-trend-header {
  font-size: $font-size-xl;
  font-weight: 300;
  color: $secondary-color;
  font-weight: bold;
  // -webkit-text-fill-color: $important-text-color; /* Will override color (regardless of order) */

  -webkit-text-stroke-width: 0.7px;

  -webkit-text-stroke-color: black;
  margin-bottom: 0;
}
</style>
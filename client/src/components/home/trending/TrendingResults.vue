<template>
  <section id="trending-results">
    <h1>Trending Results</h1>
    <article
      v-if="getTrendingFlags.results && getTrendingFlags.results.items"
      v-for="item in getTrendingFlags.results.items"
    >{{JSON.stringify(item)}}</article>
  </section>
</template>
<script>
console.log("module: TrendingResults.vue");
const { mapGetters } = require("vuex");
export default {
  name: "trending-results",
  computed: mapGetters(["getTrendingFlags"])
};
</script>
<style lang="scss" scoped>
</style>
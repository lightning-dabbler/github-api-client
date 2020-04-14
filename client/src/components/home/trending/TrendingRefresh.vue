<template>
  <section id="trending-refresh">
    <h1>Trending Refresh</h1>
    <article
      v-if="getTrendingFlags.results && getTrendingFlags.results.headers"
    >{{getTrendingFlags.results.headers.date}}</article>
    <button @click="refreshTrending">Refresh</button>
  </section>
</template>
<script>
console.log("module: TrendingRefresh.vue");
const { mapGetters } = require("vuex");
export default {
  name: "trending-refresh",
  computed: mapGetters(["getTrendingFlags"]),
  methods: {
    refreshTrending: async function refreshTrending() {
      const since =
        this.$route.query &&
        ["daily", "weekly", "monthly"].includes(this.$route.query.since)
          ? this.$route.query.since
          : "daily";
      const developers =
        this.$route.query && this.$route.query.developers === true
          ? true
          : false;
      await this.$store.dispatch("callTrending", {
        developers,
        since,
        refresh: true
      });
    }
  }
};
</script>
<style lang="scss" scoped>
</style>
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
      console.log('REFRESH')
      const since =
        this.getTrendingFlags.since &&
        ["daily", "weekly", "monthly"].includes(this.getTrendingFlags.since)
          ? this.getTrendingFlags.since
          : "daily";
      const developers =
        this.getTrendingFlags.active.developers && this.getTrendingFlags.active.developers === true
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
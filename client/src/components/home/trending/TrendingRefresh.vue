<template>
  <section id="trending-refresh">
    <button @click="refreshTrending">Refresh</button>
    <article
      v-if="getTrendingFlags.results && getTrendingFlags.results.headers"
    >Last Pulled: {{getTrendingFlags.results.headers.date}}</article>
    
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
@import "@/static/css/custom.scss";

#trending-refresh{
  border-bottom: 1px solid $ternary-color;
}
</style>
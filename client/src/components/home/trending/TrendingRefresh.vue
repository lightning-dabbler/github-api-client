<template>
  <section id="trending-refresh" class="container">
    <div class="row align-items-center">
      <div class="col-md-6 text-center mb-1">
        <button
          type="button"
          class="refresh-button btn btn-light"
          @click.prevent="refreshTrending"
        >
          <span class="refresh-symbol">Refresh</span>
        </button>
      </div>
      <div class="col-md-6 text-center mb-1">
        <p class="last-pulled mb-0" v-if="getTrendingFlags.headers">
          <span class="font-weight-bold">Last Pulled:</span>
          {{ getTrendingFlags.headers.date || getTrendingFlags.headers.Date }}
        </p>
      </div>
    </div>
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
      console.log("REFRESH");
      this.$store.commit("updateTrendingLoader", true);
      const since =
        this.getTrendingFlags.since &&
        ["daily", "weekly", "monthly"].includes(this.getTrendingFlags.since)
          ? this.getTrendingFlags.since
          : "daily";
      const developers =
        this.getTrendingFlags.active.developers &&
        this.getTrendingFlags.active.developers === true
          ? true
          : false;
      await this.$store.dispatch("callTrending", {
        developers,
        since,
        refresh: true,
      });
      this.$store.commit("updateTrendingLoader", false);
    },
  },
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";
$last-pulled-bg-color: #def7d1;
$hover-refresh-button: #e8ede5;

#trending-refresh {
  border-bottom: 1px solid $ternary-color;
}
.refresh-button {
  background-color: $primary-color;
  color: black;
}
.refresh-button:hover {
  background-color: $hover-refresh-button;
}
.last-pulled {
  background-color: $last-pulled-bg-color;
}

span.refresh-symbol::before {
  content: "";
  background-image: url(/static/images/refresh.svg);
  width: 18px;
  height: 18px;
  background-color: transparent;
  background-size: cover;
  display: inline-block;
  margin-bottom: -0.217rem;
  margin-left: -0.1rem;
}
</style>
<template>
  <section id="trending-results">
    <section v-if="items" class="text-center">
      <trending-card-dev
        v-if="active.developers"
        v-for="(item, index) in items"
        :index="index"
        :avatar="item.avatar"
        :name="item.name"
        :popular_repository="item.popular_repository"
        :profile="item.profile"
        :username="item.username"
        :key="index"
      ></trending-card-dev>
      <article v-else>
        <section v-for="item in items">{{JSON.stringify(item)}}</section>
      </article>
    </section>
  </section>
</template>
<script>
console.log("module: TrendingResults.vue");
import TrendingCardDev from "./trendingCard/TrendingCardDev.vue";
const { mapGetters } = require("vuex");
export default {
  name: "trending-results",
  components: {
    TrendingCardDev
  },
  data() {
    return { items: false, active: false };
  },
  computed: mapGetters(["getTrendingFlags"]),
  watch: {
    getTrendingFlags: {
      immediate: true,
      deep: true,
      handler() {
        this.items = this.getTrendingFlags.items;
        this.active = this.getTrendingFlags.active;
      }
    }
  }
};
</script>
<style lang="scss" scoped>
</style>
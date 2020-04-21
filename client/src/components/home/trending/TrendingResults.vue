<template>
  <section v-if="items" id="trending-results" class="text-center">
    <section v-if="active.developers">
      <trending-card-dev
        v-for="(item, index) in items"
        :index="index"
        :avatar="item.avatar"
        :name="item.name"
        :popular_repository="item.popular_repository"
        :profile="item.profile"
        :username="item.username"
        :key="index"
      ></trending-card-dev>
    </section>
    <section v-else>
      <trending-card-repo
        v-for="(item,index) in items"
        :author="item.author"
        :avatar="item.avatar"
        :built_by="item.built_by"
        :description="item.description"
        :forks="item.forks"
        :stars="item.stars"
        :language_color="item.language_color"
        :name="item.name"
        :present_freq_stars="item.present_freq_stars"
        :programming_language="item.programming_language"
        :repo_url="item.url"
        :key="index"
      ></trending-card-repo>
    </section>
  </section>
</template>
<script>
console.log("module: TrendingResults.vue");
import TrendingCardDev from "./trendingCard/TrendingCardDev.vue";
import TrendingCardRepo from "./trendingCard/TrendingCardRepo.vue";
const { mapGetters } = require("vuex");
export default {
  name: "trending-results",
  components: {
    TrendingCardDev,
    TrendingCardRepo
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
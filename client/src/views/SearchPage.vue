<template>
  <div id="search">
    <search-header></search-header>
    <section class="container py-5">
      <search-results></search-results>
    </section>
  </div>
</template>

<script>
console.info("module: search.vue");
import SearchResults from "../components/search/SearchResults.vue";
import SearchHeader from "../components/search/SearchHeader.vue";
export default {
  name: "search",
  components: {
    SearchResults,
    SearchHeader
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
</style>
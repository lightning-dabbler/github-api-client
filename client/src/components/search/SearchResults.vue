<template>
  <section id="search-results" class="search-rect text-center">
    <section v-if="payload">
      <section v-if="payload.endpoint==='repositories' && payload.items">
        <section class="py-3 results-length">
          <p class="mb-0 results-text mx-auto">{{payload.length}} Repository Result(s)!</p>
        </section>
        <search-results-repos
          v-for="(item,index) in payload.items"
          :forks_count="item.forks_count"
          :stargazers_count="item.stargazers_count"
          :watchers_count="item.watchers_count"
          :html_url="item.html_url"
          :language="item.language"
          :description="item.description"
          :name="item.name"
          :owner="item.owner"
          :index="index +1"
          :key="index"
        ></search-results-repos>
      </section>
      <section v-else-if="payload.endpoint==='users' && payload.items">
        <section class="py-3 results-length">
          <p class="mb-0 results-text mx-auto">{{payload.length}} User Result(s)!</p>
        </section>
      </section>
      <section v-else-if="payload.endpoint==='commits' && payload.items">
        <section class="py-3 results-length">
          <p class="mb-0 results-text mx-auto">{{payload.length}} Commit Result(s)!</p>
        </section>
      </section>
    </section>
  </section>
</template>
<script>
import SearchResultsCommits from "./searchResults/SearchResultsCommits.vue";
import SearchResultsRepos from "./searchResults/SearchResultsRepos.vue";
import SearchResultsUsers from "./searchResults/SearchResultsUsers.vue";
import { mapGetters } from "vuex";
export default {
  name: "search-results",
  components: {
    SearchResultsCommits,
    SearchResultsRepos,
    SearchResultsUsers
  },
  data() {
    return { payload: false };
  },
  computed: mapGetters(["getSearchPayload"]),
  watch: {
    getSearchPayload: {
      immediate: true,
      deep: true,
      handler() {
        this.payload = this.getSearchPayload;
      }
    }
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";
$results-bg-color: #def7d1;

.search-rect {
  background-color: transparent;
  border: 1px solid $ternary-color;
  border-radius: 3px;
}

#search-results {
  -webkit-user-select: none; /* Chrome/Safari */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+ */

  /* Rules below not implemented in browsers yet */
  -o-user-select: none;
  user-select: none;
}

.results-length {
  border-bottom: 1px solid $ternary-color;
  font-size: $font-size-sm;
}
.results-text {
  max-width: 300px;
  background-color: $results-bg-color;
  font-weight: bold;
}
</style>
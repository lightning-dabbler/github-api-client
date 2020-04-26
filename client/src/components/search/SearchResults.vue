<template>
  <section id="search-results" class="search-rect text-center">
    <section v-if="payload">
      <section class="py-3 results-length" v-if="payload.status_code === 422 && !payload.length">
        <p class="mb-0 bg-warning warning-text mx-auto">
          Unprocessible Entry(ies) Please Review
          <a
            href="https://developer.github.com/v3/search"
            target="_blank"
          >GitHub API</a>
        </p>
      </section>
      <section class="py-3 results-length" v-else-if="payload.status_code === 403 && !payload.length">
        <p class="mb-0 bg-warning warning-text mx-auto">Please wait ~60 seconds to reuse!</p>
      </section>
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
          <search-results-users
            v-for="(item,index) in payload.items"
            :avatar_url="item.avatar_url"
            :html_url="item.html_url"
            :login="item.login"
            :index="index+1"
            :key="index"
          ></search-results-users>
        </section>
      </section>
      <section v-else-if="payload.endpoint==='commits' && payload.items">
        <section class="py-3 results-length">
          <p class="mb-0 results-text mx-auto">{{payload.length}} Commit Result(s)!</p>
          <search-results-commits
            v-for="(item,index) in payload.items"
            :commit="item.commit"
            :html_url="item.html_url"
            :repository="item.repository"
            :index="index +1"
            :key="index"
          ></search-results-commits>
        </section>
      </section>
      <section class="py-2 vld-parent d-flex justify-content-center align-items-center" v-if="payload.load_more">
        <button type="button" class="btn btn-success" @click.prevent="loadMore">Load Next Page</button>
        <vue-loading
          :active.sync="getSearchBoxLoader.active"
          :can-cancel="getSearchBoxLoader.canCancel"
          :is-full-page="getSearchBoxLoader.isFullPage"
          :color="getSearchBoxLoader.color"
          loader="bars"
          :width="30"
          :height="30"
          :background-color="getSearchBoxLoader.backgroundColor"
          :opacity="0.8"
          :z-index="getSearchBoxLoader.zIndex"
        ></vue-loading>
      </section>
    </section>
  </section>
</template>
<script>
import SearchResultsCommits from "./searchResults/SearchResultsCommits.vue";
import SearchResultsRepos from "./searchResults/SearchResultsRepos.vue";
import SearchResultsUsers from "./searchResults/SearchResultsUsers.vue";
import VueLoading from "vue-loading-overlay";
import { mapGetters } from "vuex";
export default {
  name: "search-results",
  components: {
    SearchResultsCommits,
    SearchResultsRepos,
    SearchResultsUsers,
    VueLoading
  },
  data() {
    return { payload: false };
  },
  computed: mapGetters(["getSearchPayload", "getSearchBoxLoader"]),
  watch: {
    getSearchPayload: {
      immediate: true,
      deep: true,
      handler() {
        this.payload = this.getSearchPayload;
      }
    }
  },
  methods: {
    loadMore: async function loadMore() {
      console.log("Loading More Data");
      this.$store.commit("updateSearchBoxLoader", true);
      await this.$store.dispatch("callSearch", {});
      this.$store.commit("updateSearchBoxLoader", false);
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

.warning-text {
  max-width: 300px;
  font-weight: bold;
}
</style>
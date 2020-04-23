<template>
  <section id="search-header" class="container-fluid container">
    <header class="py-3 text-center">
      <h1 class="search-header-title mb-2">Search</h1>
      <search-box></search-box>
    </header>
  </section>
</template>
<script>
console.log("module: SearchHeader.vue");
import SearchBox from "./searchBox/SearchBox.vue";

export default {
  name: "search-header",
  components: {
    SearchBox
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";
#search-header {
  background-color: $primary-color;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("/static/images/computer-bg-img.jpg");
  background-position: center center;
  background-size: cover;
  width: 100%;
  max-width: 1024px;
  // height: 300px;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;

  .search-header-title {
    font-size: $font-size-xl;
    color: white;
    font-weight: bold;
  }
}
</style>
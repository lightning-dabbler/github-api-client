<template>
  <section id="trending-header" class="container-fluid container">
    <header class="py-3 text-center">
      <h1 class="gh-trend-header-title">Trending</h1>
      <p
        class="gh-trend-header-body mx-auto my-1 "
      >GitHub's Trending Developers and Repositories</p>
    </header>
  </section>
</template>
<script>
console.log("module: TrendingHeaders.vue");
export default {};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

#trending-header {
  background-color: $primary-color;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("/static/images/circuit-bg-img.jpg");
  background-position: center center;
  background-size: cover;
  
  width: 100%;
  max-width: 1024px;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.gh-trend-header-title {
  font-size: $font-size-xl;
  color: white;
  font-weight: bold;
  margin-bottom: 0;
}
.gh-trend-header-body {
  font-size: $font-size-sm;
  font-weight: 200;
  color: white;
  max-width: 300px;
}
</style>
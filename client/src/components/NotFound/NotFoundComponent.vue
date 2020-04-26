<template>
  <section class="text-center">
    <div class="row mt-5">
      <div class="col">
        <h1 class="font-weight-bold">404 - NOT FOUND</h1>
      </div>
    </div>
    <div class="row mt-3">
      <div class="col">
        <img src="/static/images/404.svg" class="img-fluid error-404" alt="404 - ERROR" />
      </div>
    </div>
    <div class="row mt-4">
      <div class="col">
        <h4 class="font-weight-light">This is an invalid web page.</h4>
      </div>
    </div>
    <div class="row mt-2">
      <div class="col">
        <h4 class="font-weight-light">
          Head Back
          <router-link to="/" tag="a" class="badge badge-success font-weight-bold" name="Home">Home</router-link>
        </h4>
      </div>
    </div>
  </section>
</template>

<script>
console.log("module: NotFoundComponent.vue")
export default {
  name: "not-found-component"
};
</script>
<style lang="scss" scoped>
.error-404 {
  max-width: 150px;
  max-height: 150px;
}
</style>
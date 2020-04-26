<template>
  <div id="not-found" class="container mb-5">
    <not-found-component></not-found-component>
  </div>
</template>

<script>
console.info("module: notFound.vue");
import NotFoundComponent from "../components/NotFound/NotFoundComponent.vue";
export default {
  name: "not-found",
  components: {
    NotFoundComponent
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
</style>
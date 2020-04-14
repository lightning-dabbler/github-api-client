<template>
  <section id="home">
    <trending-section></trending-section>
  </section>
</template>

<script>
console.info("module: home.vue");
import TrendingSection from "../components/home/TrendingSection.vue";

export default {
  name: "home",
  components: { TrendingSection },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
</style>
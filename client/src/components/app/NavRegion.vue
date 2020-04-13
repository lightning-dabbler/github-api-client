<template>
  <nav class="navbar navbar-expand-lg" v-lazy-container="{selector:'img'}">
    <section class="container">
      <router-link
        to="/"
        tag="a"
        name="home"
        id="emoji-nav"
        v-if="emoji_obj && emoji_obj[emoji]"
        :style="{backgroundImage:`url(${emoji_obj[emoji]})`}"
      />
      <router-link to="/search" tag="a" name="search">Search</router-link>
    </section>
  </nav>
</template>
<script>
export default {
  name: "nav-region",
  props: { emoji: String },
  data: function() {
    return {
      emoji_obj:false
    };
  },
  created: async function created() {
    await this.$store.dispatch("callGetEmoji",this.emoji);
    this.emoji_obj = this.$store.getters.getEmoji(this.emoji)
  }
};
</script>
<style lang="scss" scoped>
a#emoji-nav {
  width: 60px;
  height: 60px;
  background-color: transparent;
  background-size: cover;
}
</style>
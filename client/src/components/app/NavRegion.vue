<template>
  <nav class="navbar" v-lazy-container="{selector:'img'}">
    <section class="container">
      <router-link
        to="/"
        tag="a"
        name="home"
        class="navbar-brand"
        id="emoji-nav"
        v-if="emoji_obj && emoji_obj[emoji]"
        :style="{backgroundImage:`url(${emoji_obj[emoji]})`}"
      />
        <ul class="nav mx-auto">
          <li class="nav-item">
            <router-link to="/search" tag="a" class="nav-link direct-link direct-search" name="search"/>
          </li>
          <li class="nav-item">
            <router-link to="/" tag="a" class="nav-link direct-link direct-home" name="Home"/>
          </li>
          <li class="nav-item">
            <a
              class="nav-link direct-gh direct-link"
              name="Help"
              href="https://developer.github.com/v3/search"
              target="_blank"
            />
          </li>
        </ul>
      </section>
  </nav>
</template>
<script>

export default {
  name: "nav-region",
  props: { emoji: String },
  data: function() {
    return {
      emoji_obj: false
    };
  },
  created: async function created() {
    await this.$store.dispatch("callGetEmoji", this.emoji);
    this.emoji_obj = this.$store.getters.getEmoji(this.emoji);
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

#emoji-nav {
  width: 60px;
  height: 60px;
  background-color: transparent;
  background-size: cover;
}

.nav-link.direct-link {
  width: 30px;
  height: 30px;
  background-size: cover;
  display: inline-block;
  // margin-right: -0.1rem;
  // margin-top: -0.2rem;
}
.direct-home {
  background-image: url("/static/images/home.svg");
}
.direct-gh {
  background-image: url("/static/images/help.svg");
}
.direct-search{
background-image: url("/static/images/search.svg");
}

.nav-link {
  display:inline;
}


</style>
<template>
  <nav class="navbar" v-lazy-container="{selector:'img'}">
    <section class="container">
      <section class="mx-auto wrapper-nav-items">
      <router-link
        to="/"
        tag="a"
        name="home"
        class="navbar-brand d-inline-block my-1"
        id="emoji-nav"
        v-if="emoji_obj && emoji_obj[emoji]"
        v-lazy:background-image="emoji_obj[emoji]"
      />
      <ul
        class="nav mr-auto my-1"
      >

        <li class="nav-item">
          <router-link to="/search" tag="a" class="nav-link" name="search">
            <img class="direct-link" :data-src="'/static/images/search.svg'" />Search
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/" tag="a" class="nav-link" name="Home">
            <img class="direct-link" :data-src="'/static/images/home.svg'" />Home
          </router-link>
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            href="https://developer.github.com/v3/search"
            target="_blank"
          >
            <img class="direct-link" :data-src="'/static/images/help.svg'" />Help
          </a>
        </li>
      </ul>
      </section>
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
.wrapper-nav-items{
  display: flex;
    align-items: center;
}
#emoji-nav {
  width: 60px;
  height: 60px;
  background-color: transparent;
  background-size: cover;
  margin: 0;
}

img.direct-link {
  width: 25px;
  height: 25px;
  margin-top: -0.4rem;
}

.nav-link {
  display: inline;
  padding: 0.2rem;
}

@media all and (max-width: 350px) {
  .wrapper-nav-items{
    display:block;
    text-align:center;
  }
  #emoji-nav {
    margin-left: auto;
    margin-right: auto;
  }
  .nav {
    justify-content: center;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
<template>
  <nav class="navbar" v-lazy-container="{selector:'img'}">
    <section class="container">
      <router-link
        to="/"
        tag="a"
        name="home"
        class="navbar-brand d-inline-block my-1"
        id="emoji-nav"
        v-if="emoji_obj && emoji_obj[emoji]"
        :style="{backgroundImage:`url(${emoji_obj[emoji]})`}"
      />
      <ul class="nav mr-auto my-1">
        <!-- <li class="nav-item">
          
        </li>-->

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
            name="Help"
            href="https://developer.github.com/v3/search"
            target="_blank"
          >
            <img class="direct-link" :data-src="'/static/images/help.svg'" />Help
          </a>
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
  margin: 0;
  margin-left: auto;
}

img.direct-link {
  width: 25px;
  height: 25px;
  margin-top: -0.4rem;
}
// .nav,.nav-link {
//   // float: right;
//   display: flex;
//   justify-content: center;
//   align-items: center;
// }
.nav-link {
  display: inline;
  padding: 0.2rem;
}

.nav {
  margin-right: auto;
}

@media all and (max-width: 350px) {
  #emoji-nav {
    margin-left: auto;
    margin-right: auto;
  }
  .nav {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
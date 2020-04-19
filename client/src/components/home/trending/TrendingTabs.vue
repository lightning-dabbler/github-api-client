<template>
  <section id="trending-tabs">
    <ul class="nav nav-pills" v-if="active">
      <li class="nav-item">
        <button
          :class="`nav-link ${active.repositories?'active':''}`"
          @click.prevent="updateTrendType('repositories')"
        >Repositories</button>
      </li>
      <li class="nav-item">
        <button
          :class="`nav-link ${active.developers?'active':''}`"
          @click.prevent="updateTrendType('developers')"
        >Developers</button>
      </li>
      <li v-if="curr_since" class="nav-item dropdown">
        <button
          class="nav-link dropdown-toggle"
          data-toggle="dropdown"
          role="button"
          aria-haspopup="true"
          aria-expanded="false"
        >{{curr_since}}</button>
        <div class="dropdown-menu">
          <button
            v-for="item in since_arr"
            v-if="item !== curr_since"
            class="dropdown-item"
            @click.prevent="updateSince(item)"
          >{{item}}</button>
        </div>
      </li>
    </ul>
  </section>
</template>
<script>
console.log("module: TrendingTabs.vue");

export default {
  name: "trending-tabs",
  data() {
    return {
      active: false,
      curr_since: false,
      since_arr: false
    };
  },
  created: async function created() {
    console.log("TrendingHeader.vue: created");
    await this.mountData();
  },
  methods: {
    updateRoute(since,developers){
      if (since == "daily") {
        this.$router.replace({ name: "landing", query: { developers } });
      } else {
        this.$router.replace({ name: "landing", query: { developers, since } });
      }
    },
    mountData: async function mountData() {
      this.$store.commit("updateTrendingLoader",true)
      const since =
        this.$route.query &&
        ["daily", "weekly", "monthly"].includes(this.$route.query.since)
          ? this.$route.query.since
          : "daily";
      const developers =
        this.$route.query &&
        (this.$route.query.developers == true ||
          this.$route.query.developers == "true")
          ? true
          : false;

      const repositories = !developers;
      const payload = {
        active: {
          developers,
          repositories
        },
        since
      };
      this.curr_since = since.charAt(0).toUpperCase() + since.slice(1);
      this.since_arr = ["Daily", "Weekly", "Monthly"];
      this.active = payload.active;
      this.$store.commit("updateTrendingFlags", payload);
      await this.$store.dispatch("callTrending", {
        developers: payload.active.developers,
        since: payload.since
      });
      this.$store.commit("updateTrendingLoader",false)
    },
    updateSince: async function updateSince(freq) {
      console.log("TrendingHeader.vue: updateSince")
      this.$store.commit("updateTrendingLoader",true)
      const developers = this.active.developers;
      const since = freq.toLowerCase();
      this.$store.commit("updateTrendingFlags", { since });
      await this.$store.dispatch("callTrending", { developers, since });
      this.curr_since = freq;
      this.updateRoute(since,developers)
      this.$store.commit("updateTrendingLoader",false)
    },
    updateTrendType: async function updateTrendType(name) {
      console.log("TrendingHeader.vue: updateTrendType")
      let developers = this.active.developers;
      const since = this.curr_since.toLowerCase();
      if (developers && name === "developers") {
        return;
      } else if (developers && name == "repositories") {
        this.$store.commit("updateTrendingLoader",true)
        developers = false;
        const repositories = true;
        const payload = {
          active: {
            developers,
            repositories
          }
        };
        this.$store.commit("updateTrendingFlags", payload);
        await this.$store.dispatch("callTrending", { developers, since });
      } else if (!developers && name === "repositories") {
        return;
      } else {
        this.$store.commit("updateTrendingLoader",true)
        developers = true;
        const repositories = false;
        const payload = {
          active: {
            developers,
            repositories
          }
        };
        this.$store.commit("updateTrendingFlags", payload);
        await this.$store.dispatch("callTrending", { developers, since });
      }
      this.active.developers = developers;
      this.active.repositories = !developers;
      this.updateRoute(since,developers)
      this.$store.commit("updateTrendingLoader",false)
    }
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

.nav-link {
  padding: 0.5rem;
}
.dropdown-menu {
  min-width: 8rem;
}
.nav-link,
.dropdown-item {
  color: black;
  background-color: transparent;
  outline: none;
  border: none;
  text-decoration: none;
}
.nav-pills .nav-link.active {
  color: white;
  background-color: $secondary-color;
}
.nav-pills .show > .nav-link {
  color: $secondary-color;
  background-color: transparent;
}

.dropdown-item.active,
.dropdown-item:active {
  color: white;
  text-decoration: none;
  background-color: $secondary-color;
}
div.dropdown-menu.show,
div.dropdown-menu {
  padding: 0;
}
.dropdown-item:first-child {
  padding-top: $font-size-xs;
}
.dropdown-item:nth-child(2) {
  padding-bottom: $font-size-xs;
}
#trending-tabs {
  border-bottom: 1px solid $ternary-color;
  background-color: $primary-color;
}

@media all and (max-width: 991px) {
  #trending-tabs {
    display: flex;
    justify-content: center;
  }
}
@media all and (max-width: 245px){
  #trending-tabs {
    display:block
  }
  .nav-item {
    display:inline-block;
    margin:0 auto;
  }
}
</style>
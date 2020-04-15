<template>
  <section id="trending-tabs">
    <ul class="nav nav-pills" v-if="active">
      <li class="nav-item">
        <button
          :class="`nav-link ${active.repositories?'active':''}`"
          @click="updateTrendType('repositories')"
        >Repositories</button>
      </li>
      <li class="nav-item">
        <button
          :class="`nav-link ${active.developers?'active':''}`"
          @click="updateTrendType('developers')"
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
            @click="updateSince(item)"
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
  },
  methods: {
    updateSince: async function updateSince(freq) {
      const developers = this.active.developers;
      const since = freq.toLowerCase();
      this.$store.commit("updateTrendingFlags", { since });
      await this.$store.dispatch("callTrending", { developers, since });
      this.curr_since = freq;
      if (since == "daily") {
        this.$router.push({ name: "landing", query: { developers } });
      } else {
        this.$router.push({ name: "landing", query: { developers, since } });
      }
    },
    updateTrendType: async function updateTrendType(name) {
      let developers = this.active.developers;
      const since = this.curr_since.toLowerCase();
      if (developers && name === "developers") {
        return;
      } else if (developers && name == "repositories") {
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
      if (since == "daily") {
        this.$router.push({ name: "landing", query: { developers } });
      } else {
        this.$router.push({ name: "landing", query: { developers, since } });
      }
    }
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

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
</style>
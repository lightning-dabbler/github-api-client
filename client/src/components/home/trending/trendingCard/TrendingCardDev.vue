<template>
  <article>
    <section id="trending-card-dev" class="card bg-light text-center">
      <div class="card-header text-left">
        <img
          :src="`/static/images/trending_up.svg`"
          alt="Trending Up"
          class="img-fluid trending-up"
        />
        {{index+1}}
      </div>
      <div class="card-body">
        <div class="card-title mb-2">
          <a
            class="card-link font-weight-bold full-name"
            :href="profile"
            target="_blank"
          >{{name.length > 20? name.slice(0,17)+'...':name}}</a>
        </div>
        <div class="card-subtitle mb-3">
          <a
            class="card-link username-profile font-weight-normal"
            :href="profile"
            target="_blank"
          >{{username}}</a>
        </div>
        <a :href="profile" target="_blank">
          <img :src="avatar" :alt="username" class="card-img-top avatar-img img-fluid" />
        </a>
        <div
          v-if="popular_repository"
          class="card-title text-muted mt-2 mb-0 font-weight-normal popular-repo-title"
        >Popular Repo:</div>
        <a
          v-if="popular_repository"
          class="card-subtitle card-link font-weight-bold repo-name"
          :href="popular_repository.url"
          target="_blank"
        >{{popular_repository.name.length > 20?popular_repository.name.slice(0,17)+'...':popular_repository.name}}</a>
        <p
          v-if="popular_repository && popular_repository.description"
          class="card-text text-muted mb-1 font-weight-light"
        >{{popular_repository.description.length > 125?popular_repository.description.slice(0,120)+'...' :popular_repository.description}}</p>
      </div>
    </section>
  </article>
</template>

<script>
console.log("Module: TrendingCardDev.vue");
export default {
  name: "trending-card-dev",
  props: {
    index: Number,
    avatar: String,
    name: String,
    popular_repository: Object,
    profile: String,
    username: String
  }
};
</script>

<style lang="scss" scoped>
@import "@/static/css/custom.scss";

article {
  width: 300px;
  display: inline-grid;
  margin: 1rem;
  border: 1px solid $ternary-color;
  border-radius: .25rem;
}
.card {
  font-size: $font-size-sm;
  border:none;
}

article:hover {
  box-shadow: $trending-card-hover;
}

.card-header {
  border-bottom: 1px solid $ternary-color;
}

.username-profile {
  color: $secondary-color;
}

.full-name {
  font-size: $font-size-m;
}

.avatar-img {
  width: 100px;
  height: 100px;
}
.trending-up {
  width: 24px;
  height: 24px;
}

.repo-name::before {
  background-image: url("/static/images/repo.svg");
  margin-bottom: -0.18rem;
}
.popular-repo-title:before {
  background-image: url("/static/images/fire.svg");
  margin-bottom: -0.1rem;
}

.repo-name::before,
.popular-repo-title:before {
  content: "";
  background-size: contain;
  width: $font-size-sm;
  height: $font-size-sm;
  display: inline-block;
  background-repeat: no-repeat;
}

@media all and (max-width: 370px) {
  article {
    width: 90%;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
<template>
  <section id="trending-card-dev" class="card bg-light text-center">
    <div class="card-header text-left">
      <img :src="`/static/images/trending_up.svg`" alt="Trending Up" class="img-fluid trending-up" />
      {{index+1}}
    </div>
    <div class="card-body">
      <div class="card-title mb-2">
        <a
          class="card-link font-weight-bold full-name"
          :href="profile"
          :name="name"
          target="_blank"
        >{{name.length > 20? name.slice(0,17)+'...':name}}</a>
      </div>
      <div class="card-subtitle">
        <a
          class="card-link d-block ml-0 mb-3 username-profile font-weight-normal"
          :href="profile"
          :name="username"
          target="_blank"
        >{{username}}</a>
      </div>
      <a :href="profile" target="_blank">
        <img :src="avatar" :alt="username" class="card-img-top avatar-img img-fluid" />
      </a>
      <div class="card-title text-muted mt-2 mb-0 font-weight-normal">Popular Repo:</div>
      <a
        class="card-subtitle card-link font-weight-bold repo-name"
        :href="popular_repository.url"
        target="_blank"
      >{{popular_repository.name.length > 20?popular_repository.name.slice(0,17)+'...':popular_repository.name}}</a>
      <p
        class="card-text text-muted mb-1 font-weight-light"
      >{{popular_repository.description && popular_repository.description.length > 125?popular_repository.description.slice(0,120)+'...' :popular_repository.description}}</p>
    </div>
  </section>
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
.card {
  width: 300px;
  display: inline-grid;
  margin: 1rem;
  font-size: $font-size-sm;
  border: 1px solid $ternary-color;
}

.card:hover {
      box-shadow: $trending-card-hover;
}

.card-header{
    border-bottom: 1px solid $ternary-color;;
}

.username-profile {
    color:$secondary-color;
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
content:"";
background-image: url("/static/images/repo.svg");
background-size:contain;
width: $font-size-sm;
height: $font-size-sm;
display: inline-block;
background-repeat:no-repeat;
margin-bottom: -0.18rem;
}

@media all and (max-width: 370px) {
  .card {
    width: 90%;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
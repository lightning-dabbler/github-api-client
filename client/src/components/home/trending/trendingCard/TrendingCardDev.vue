<template>
  <section id="trending-card-dev" class="card bg-light text-center">
    <div class="card-body">
        <a
      class="card-title card-link"
      :href="profile"
      :name="name"
      target="_blank"
    >{{index+1}}|{{name}}</a>
      <a
        class="card-subtitle card-link d-block ml-0"
        :href="profile"
        :name="username"
        target="_blank"
      >{{username}}</a>
      <a :href="profile" target="_blank">
        <img :src="avatar" :alt="username" class="card-img-top avatar-img img-fluid" />
      </a>
        <div class="card-title text-muted mt-2 mb-0">Popular Repo:</div>
        <a
          class="card-subtitle card-link"
          :href="popular_repository.url"
          target="_blank"
        >{{popular_repository.name.length > 20?popular_repository.name.slice(0,17)+'...':popular_repository.name}}</a>
        <p
          class="card-text text-muted mb-1"
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
.card {
  width: 300px;
  display: inline-grid;
  margin: 1rem;
}
// .card-body {
//     height: 300px;
// }
.avatar-img {
  width: 100px;
  height: 100px;
}

@media all and (max-width: 370px) {
    .card {
        width:90%;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
}


</style>
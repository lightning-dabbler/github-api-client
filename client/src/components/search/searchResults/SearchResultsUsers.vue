<template>
  <article>
    <section id="search-results-users" class="card bg-light text-center">
      <div class="card-body">
        <div class="card-title">
          <a class="card-link font-weight-bold" :href="html_url" target="_blank">{{login}}</a>
        </div>
        <a :href="html_url" target="_blank">
          <img :src="avatar_url" :alt="login" class="card-img-top avatar-img img-fluid" />
        </a>
      </div>
      <div class="card-footer text-left text-muted">{{index}}</div>
    </section>
  </article>
</template>
<script>
export default {
  name: "search-results-users",
  props: {
    avatar_url: String,
    html_url: String,
    login: String,
    index: Number
  }
};
</script>

<style lang="scss" scoped>
@import "@/static/css/custom.scss";

article {
  display: inline-grid;
  width: 225px;
  margin: 1rem;
  border: 1px solid $ternary-color;
  border-radius: .25rem;
}

.card {
  font-size: $font-size-sm;
  border:none;
}
.card-title {
    font-size: $font-size-m;
}

article:hover {
  box-shadow: $trending-card-hover;
}

.avatar-img {
  width: 100px;
  height: 100px;
}

@media all and (max-width: 295px) {
  article {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 90%;
  }
}
</style>
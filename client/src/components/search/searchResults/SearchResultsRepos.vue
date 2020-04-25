<template>
  <article id="search-results-repos" class="card bg-light text-center">
    <div class="card-body">
      <div class="card-title">
        <a
          class="card-link repo-result font-weight-bold"
          :alt="name"
          :href="html_url"
          target="_blank"
        >{{name.length > 25? name.slice(0,22)+'...':name}}</a>
      </div>
      <p
        class="card-text text-muted mb-2 font-weight-light"
      >{{description && description.length > 125?description.slice(0,120)+'...' :description}}</p>
      <a :href="owner.html_url" target="_blank">
          <img :src="owner.avatar_url" :alt="owner.login" class="card-img-top avatar-img img-fluid" />
      </a>
      <p class="card-subtitle mt-2">{{owner.login}}</p>
      <p v-if="language">Language: {{language}}</p>
      <div class="row my-2 text-muted">
        <div class="col-sm-4">
          <p class="repo-watchers mb-0">
            {{watchers_count}}
          </p>
        </div>
        <div class="col-sm-4">
          <p class="repo-stars mb-0">{{stargazers_count}}</p>
        </div>
        <div class="col-sm-4">
          <p class="repo-forks mb-0">{{forks_count}}</p>
        </div>
      </div>
    </div>
  </article>
</template>
<script>
export default {
  /**
   * owner.avatar_url
   * owner.html_url
   * owner.login
   */
  name: "search-results-repos",
  props: {
    forks_count: Number,
    stargazers_count: Number,
    watchers_count: Number,
    html_url: String,
    language: String,
    description: String,
    name: String,
    owner: Object
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

.card {
  width: 400px;
  display: inline-grid;
  margin: 1rem;
  font-size: $font-size-sm;
  border: 1px solid $ternary-color;
}

.card:hover {
  box-shadow: $trending-card-hover;
}

.repo-result {
  font-size: $font-size-m;
}

.repo-result::before {
  background-image: url("/static/images/repo.svg");
  content: "";
  background-size: contain;
  width: $font-size-m;
  height: $font-size-m;
  display: inline-block;
  background-repeat: no-repeat;
  margin-bottom: -0.18rem;
}

.avatar-img {
  width: 100px;
  height: 100px;
}

.repo-stars::before {
  background-image: url("/static/images/star.svg");
  margin-bottom: -0.04rem;
  margin-right: 0.2rem;
}
.repo-forks::before {
  background-image: url("/static/images/fork.svg");
  margin-bottom: -0.1rem;
}

.repo-watchers::before {
background-image: url("/static/images/eye.svg");
margin-bottom: -0.1rem;
}

.repo-stars::before,
.repo-forks::before,
.repo-watchers::before {
  content: "";
  background-size: contain;
  width: $font-size-sm;
  height: $font-size-sm;
  display: inline-block;
  background-repeat: no-repeat;
}

@media all and (max-width: 470px) {
  .card {
    width: 90%;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
}

</style>
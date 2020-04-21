<template>
  <article id="trending-card-repo" class="card bg-light text-center">
    <div class="card-body">
      <div class="card-title">
        <a
          class="card-link popular-repo"
          :alt="`${author} / ${name}`"
          :href="repo_url"
          target="_blank"
        >
          {{`${author} / `}}
          <span
            class="font-weight-bold"
          >{{name.length > 25? name.slice(0,22)+'...':name}}</span>
        </a>
      </div>
      <p
        class="card-text text-muted mb-2 font-weight-light"
      >{{description && description.length > 125?description.slice(0,120)+'...' :description}}</p>
      <a :href="`https://github.com/${author}`" target="_blank">
        <img :src="avatar" :alt="author" class="card-img-top avatar-img img-fluid" />
      </a>
      <div class="row my-2 text-muted" v-if="programming_language">
        <div class="col-sm-4">
          <p class="mb-0">
            <span
              class="prog-lang-circle text-center"
              :style="{backgroundColor:`${language_color}`}"
            ></span>
            {{programming_language}}
          </p>
        </div>
        <div class="col-sm-4">
          <p class="repo-stars mb-0">{{stars}}</p>
        </div>
        <div class="col-sm-4">
          <p class="repo-forks mb-0">{{forks}}</p>
        </div>
      </div>
      <div class="text-muted my-2" v-else>
        <div class="d-inline-block">
          <p class="repo-stars mb-0 mr-2">{{stars}}</p>
        </div>
        <div class="d-inline-block">
          <p class="repo-forks mb-0 ml-2">{{forks}}</p>
        </div>
      </div>
      <p class="repo-stars text-muted">{{present_freq_stars}}</p>
    </div>
    <div class="card-footer">
      <div class="card-title text-muted font-weight-normal">Built By:</div>
      <a v-for="(worker,index) in built_by" class="d-inline-block my-2 mx-2" :key="index" :href="worker.profile" target="_blank">
        <img
          :alt="worker.username"
          :src="worker.avatar"
          class="card-img-top built-by-img img-fluid"
        />
      </a>
    </div>
  </article>
</template>
<script>
export default {
  name: "trending-card-repo",
  props: {
    author: String,
    avatar: String,
    built_by: Array,
    description: String,
    forks: Number,
    stars: Number,
    language_color: String,
    name: String,
    present_freq_stars: String,
    programming_language: String,
    repo_url: String
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

.popular-repo {
  font-size: $font-size-m;
}

.popular-repo::before {
  background-image: url("/static/images/repo.svg");
  content: "";
  background-size: contain;
  width: $font-size-m;
  height: $font-size-m;
  display: inline-block;
  background-repeat: no-repeat;
  margin-bottom: -0.18rem;
  margin-right: -0.4rem;
}
.avatar-img {
  width: 100px;
  height: 100px;
}
.prog-lang-circle {
  display: inline-block;
  border-radius: 50%;
  width: $font-size-sm;
  height: $font-size-sm;
}

.repo-stars::before {
  background-image: url("/static/images/star.svg");
  margin-bottom: -0.04rem;
  margin-right: 0.2rem;
}
.repo-forks:before {
  background-image: url("/static/images/fork.svg");
  margin-bottom: -0.1rem;
}

.repo-stars::before,
.repo-forks:before {
  content: "";
  background-size: contain;
  width: $font-size-sm;
  height: $font-size-sm;
  display: inline-block;
  background-repeat: no-repeat;
}
.built-by-img {
  width: 50px;
  height: 50px;
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
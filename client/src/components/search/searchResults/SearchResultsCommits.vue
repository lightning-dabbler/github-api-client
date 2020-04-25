<template>
  <article>
    <section id="search-results-commits" class="card bg-light text-center">
      <div class="card-body">
        <div class="card-title">
          <a
            class="card-link commit-result font-weight-bold"
            :href="html_url"
            target="_blank"
          >{{commit.message.length > 100? commit.message.slice(0,97)+'...':commit.message}}</a>
        </div>
        <div class="card-subtitle">
          <a class="repo-commit card-link" :href="repository.html_url" target="_blank">
            {{`${repository.owner.login} / `}}
            <span
              class="font-weight-bold"
            >{{repository.name.length > 25? repository.name.slice(0,22)+'...':repository.name}}</span>
          </a>
        </div>
        <div class="card-text text-muted mt-2">
          <p>{{commit.author.date}}</p>
          <p>{{commit.author.email}}</p>
          <p>{{commit.author.name}}</p>
        </div>
      </div>
      <div class="card-footer text-left text-muted">{{index}}</div>
    </section>
  </article>
</template>
<script>
export default {
  name: "search-results-commits",
  props: {
    commit: Object,
    html_url: String,
    repository: Object,
    index: Number
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

article {
  display: inline-grid;
  width: 300px;
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

.commit-result {
  font-size: $font-size-m;
}

.commit-result::before {
  background-image: url("/static/images/commit.svg");
  content: "";
  background-size: contain;
  width: $font-size-m;
  height: $font-size-m;
  display: inline-block;
  background-repeat: no-repeat;
  margin-bottom: -0.18rem;
}

.repo-commit {
  color: $secondary-color;
}
.repo-commit::before {
  content: "";
  background-size: contain;
  width: $font-size-sm;
  height: $font-size-sm;
  display: inline-block;
  background-repeat: no-repeat;
  background-image: url("/static/images/repo.svg");
  margin-bottom: -0.18rem;
}

@media all and (max-width: 370px) {
  article {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 90%;
  }
}
</style>
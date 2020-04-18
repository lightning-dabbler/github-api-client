<template>
  <footer id="footer" class="footer">
    <section class="container">
      <p class="text-center mb-0" v-if="year > 2020">
        &#169; 2020-{{year}} Osarodion Irabor
        <span
          v-if="emoji_obj && emoji_obj[emoji]"
          id="emoji-footer"
          :style="{backgroundImage:`url(${emoji_obj[emoji]})`}"
        />
      </p>
      <p class="text-center mb-0" v-else>
        &#169; 2020 Osarodion Irabor
        <span
          v-if="emoji_obj && emoji_obj[emoji]"
          id="emoji-footer"
          :style="{backgroundImage:`url(${emoji_obj[emoji]})`}"
        />
      </p>
    </section>
  </footer>
</template>
<script>
const year = new Date().toLocaleString("en-US", {
  timeZone: "America/New_York",
  year: "numeric"
});
export default {
  name: "footer-region",
  props: { emoji: String },
  data: function() {
    return {
      year,
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
footer#footer {
  font-size: $font-size-sm;
}
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px;
  line-height: 60px;
  background-color: $primary-color;
}
span#emoji-footer {
  width: 18px;
  height: 18px;
  background-color: transparent;
  background-size: cover;
  display: inline-block;
  margin-bottom: -0.2rem;
  margin-left: -0.2rem;
}
</style>
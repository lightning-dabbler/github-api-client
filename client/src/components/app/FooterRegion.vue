<template>
  <footer id="footer">
    <section class="container">
      <p class="text-center" v-if="year > 2020">
        &#169; 2020-{{year}} Osarodion Irabor
        <span
          v-if="emoji_obj && emoji_obj[emoji]"
          id="emoji-footer"
          :style="{backgroundImage:`url(${emoji_obj[emoji]})`}"
        />
      </p>
      <p class="text-center" v-else>
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
const { getEmoji } = require("../../lib/emoji");

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
    this.emoji_obj = await getEmoji(this.emoji);
  }
};
</script>
<style lang="scss" scoped>
footer#footer {
  font-size: 1rem;
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
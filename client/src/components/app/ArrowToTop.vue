<template>
  <a id="arrow-to-top" ref="arrow-to-top" @click="topFunction"></a>
</template>
<script>
console.log("module: ArrowToTop.vue");

// When Arroe clicked,
// scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // Safari
  document.documentElement.scrollTop = 0; // Chrome, Firefox and Opera
}
export default {
  name: "arrow-to-top",
  methods: {
    topFunction,
    scrollFunction: function scrollFunction(event) {
      // When the user scrolls down 30px from the top of the document, show the arrow
      if (
        document.body.scrollTop > 30 ||
        document.documentElement.scrollTop > 30
      ) {
        this.arrow.style.display = "table-cell";
      } else {
        this.arrow.style.display = "none";
      }
    }
  },
  data() {
    return { arrow: false };
  },
  mounted() {
    this.$nextTick(() => {
      this.arrow = this.$refs["arrow-to-top"];
      console.log(this.arrow);

      window.addEventListener("scroll", this.scrollFunction);
    });
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

$default-bg: #ff8b01;
$hover-bg: #4e8132;
$active-bg: #8ccd69;

#arrow-to-top {
  background-color: $default-bg;
  opacity: 0.6;
  width: 50px;
  height: 45px;
  text-align: center;
  border-radius: 4px;
  text-align: center;
  display: none;
  vertical-align: middle;
  position: fixed;
  bottom: 40px;
  right: 30px;
  -webkit-transition: background-color 0.3s;
  -moz-transition: background-color 0.3s;
  -o-transition: background-color 0.3s;
  transition: background-color 0.3s;
  z-index: 1000;
}
#arrow-to-top:hover {
  cursor: pointer;
  background-color: $hover-bg;
  opacity: 1;
}
#arrow-to-top:active {
  background-color: $active-bg;
  opacity: 0.8;
}
#arrow-to-top::after {
  content: "\21E7";
  color: #fff;
  font-weight: bold;
  font-size: $font-size-l;
}

@media all and (max-width: 400px) {
  #arrow-to-top {
    width: 40px;
    height: 35px;
  }
  #arrow-to-top::after {
    font-size: $font-size-m;
  }
}
</style>
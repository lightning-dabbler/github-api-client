<template>
  <section v-if="invalid" class="invalid-input bg-danger text-white mt-1">{{message}}</section>
</template>
<script>
export default {
  props: {
    invalid: Boolean,
    message: String
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";
.invalid-input {
    font-size: $font-size-sm;
    max-width: 250px;
    border-radius: 2px;
}

@media all and (max-width: 575px) {
  .invalid-input {
    margin-left: auto;
    margin-right: auto;
  }
}

</style>
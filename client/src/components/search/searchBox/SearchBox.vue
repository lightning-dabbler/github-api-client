<template>
  <section id="search-box" class="py-3 px-2">
    <article>
      <div class="form-group row">
        <label for="query-param" class="col-sm-3 col-form-label">Query</label>
        <div class="col-sm-9">
          <input type="text" class="form-control" id="query-param" required />
        </div>
      </div>
      <div class="form-group row">
        <label for="sort-arg" class="col-sm-3 col-form-label">Sort</label>
        <div class="col-sm-9">
          <input type="text" class="form-control" id="sort-arg" />
        </div>
      </div>
      <div class="form-row align-items-center">
        <div class="col-auto my-1" v-if="getSearchBox.type">
          <label class="mr-sm-2" for="query-type-param">Type</label>
          <select
            class="custom-select mr-sm-2"
            id="query-type-param"
            @change="modifyOptions(type_payload)"
            v-model="type_payload"
          >
            <option
              :value="{type:{selected:getSearchBox.type.selected}}"
              selected
            >{{getSearchBox.type.selected.html}}</option>
            <option
              v-for="(item,index) in getSearchBox.type.options"
              :value="{type:{selected:item}}"
              :key="index"
            >{{item.html}}</option>
          </select>
        </div>
        <div class="col-auto my-1" v-if="getSearchBox.order">
          <label class="mr-sm-2" for="order-arg">Order</label>
          <select
            class="custom-select mr-sm-2"
            id="order-arg"
            @change="modifyOptions(order_payload)"
            v-model="order_payload"
          >
            <option
              :value="{order:{selected:getSearchBox.order.selected}}"
              selected
            >{{getSearchBox.order.selected.html}}</option>
            <option
              v-for="(item,index) in getSearchBox.order.options"
              :value="{order:{selected:item}}"
              :key="index"
            >{{item.html}}</option>
          </select>
        </div>
      </div>
      <div class="mt-3">
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </article>
  </section>
</template>
<script>
console.log("module: SearchBox.vue");
const { mapGetters } = require("vuex");

export default {
  name: "search-box",
  computed: mapGetters(["getSearchBox"]),
  created() {
    this.order_payload = {
      order: { selected: this.getSearchBox.order.selected }
    };
    this.type_payload = { type: { selected: this.getSearchBox.type.selected } };
  },
  data() {
    return { order_payload: false, type_payload: false };
  },
  methods: {
    modifyOptions(payload) {
      if (
        (payload.type &&
          payload.type.selected &&
          payload.type.selected.value &&
          payload.type.selected.html) ||
        (payload.order &&
          payload.order.selected &&
          payload.order.selected.value &&
          payload.order.selected.html)
      ) {
        console.log(payload)
        this.$store.commit("updateSearchBox", payload);
      } else {
        console.log(
          `INVALID PAYLOAD @ SearchBox.vue -> modifyOptions ${JSON.stringify(
            payload
          )}`
        );
      }
    }
  }
};
</script>
<style lang="scss" scoped>
@import "@/static/css/custom.scss";

#search-box {
  // background-color: $secondary-color;
  background-color: transparent;
  border: 1px solid $ternary-color;
  border-radius: 3px;
}

label {
  font-size: $font-size-m;
  color: white;
}
input {
  font-size: $font-size-m;
  max-width: 250px;
}

@media all and (max-width: 575px) {
  input {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
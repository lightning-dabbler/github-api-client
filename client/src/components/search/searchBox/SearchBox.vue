<template>
  <section id="search-box" class="py-3 px-2">
    <article>
      <div class="form-group row">
        <label for="query-param" class="col-sm-3 col-form-label label-required">Query</label>
        <div class="col-sm-9">
          <input
            type="text"
            class="form-control"
            id="query-param"
            maxlength="100"
            size="100"
            :value="submit.query"
            @input="validateInput('query')"
            required
          />
          <invalid-input :invalid="query.invalid" :description="query.description"></invalid-input>
        </div>
      </div>
      <div class="form-group row">
        <label for="sort-arg" class="col-sm-3 col-form-label">Sort</label>
        <div class="col-sm-9">
          <input
            type="text"
            class="form-control"
            id="sort-arg"
            maxlength="100"
            size="100"
            :value="submit.sort"
            @input="validateInput('sort')"
          />
          <invalid-input :invalid="sort.invalid" :description="sort.description"></invalid-input>
        </div>
      </div>
      <div class="form-row align-items-center block-content">
        <div class="col-auto my-1 block-content" v-if="getSearchBoxSelect.type">
          <label class="mr-sm-2 block-content label-required" for="query-type-param">Type</label>
          <select
            class="custom-select mr-sm-2 block-content"
            id="query-type-param"
            @change="modifyOptions(type_payload)"
            v-model="type_payload"
          >
            <option
              :value="{type:{selected:getSearchBoxSelect.type.selected}}"
              selected
            >{{getSearchBoxSelect.type.selected.html}}</option>
            <option
              v-for="(item,index) in getSearchBoxSelect.type.options"
              :value="{type:{selected:item}}"
              :key="index"
            >{{item.html}}</option>
          </select>
        </div>
        <div class="col-auto my-1 block-content" v-if="getSearchBoxSelect.order">
          <label class="mr-sm-2 block-content" for="order-arg">Order</label>
          <select
            class="custom-select mr-sm-2 block-content"
            id="order-arg"
            @change="modifyOptions(order_payload)"
            v-model="order_payload"
          >
            <option
              :value="{order:{selected:getSearchBoxSelect.order.selected}}"
              selected
            >{{getSearchBoxSelect.order.selected.html}}</option>
            <option
              v-for="(item,index) in getSearchBoxSelect.order.options"
              :value="{order:{selected:item}}"
              :key="index"
            >{{item.html}}</option>
          </select>
        </div>
      </div>
      <div class="mt-3">
        <button
          type="button"
          class="btn btn-primary"
          :disabled="submit.disabled"
          @click.prevent="submitRequest"
        >Submit</button>
      </div>
    </article>
  </section>
</template>
<script>
console.log("module: SearchBox.vue");
const { mapGetters } = require("vuex");
import InvalidInput from "./invalid/InvalidInput.vue";

export default {
  name: "search-box",
  computed: mapGetters([
    "getSearchBoxSelect",
    "getSearchBoxValidations",
    "getSearchSubmitValues"
  ]),
  components: { InvalidInput },
  created() {
    this.order_payload = {
      order: { selected: this.getSearchBoxSelect.order.selected }
    };
    this.type_payload = {
      type: { selected: this.getSearchBoxSelect.type.selected }
    };
    this.query = this.getSearchBoxValidations.query_validation;
    this.sort = this.getSearchBoxValidations.sort_validation;
    this.submit = this.getSearchSubmitValues;
  },
  data() {
    return {
      order_payload: false,
      type_payload: false,
      query: false,
      sort: false,
      submit: false
    };
  },
  methods: {
    submitRequest() {
      console.log("Submit");
    },
    validateInput(name) {
      console.log("function: validateInput");
      name = name === "query" ? name : "sort";
      let submitPayload;
      let value = event.target.value;
      submitPayload = {};
      submitPayload[name] = value;
      value = value.trim();
      console.log(value)
      if (value.includes(" ")) {
        this.$store.commit("updateSearchBoxValidations", {
          [name]: {
            invalid: true,
            description: "Please remove whitespace."
          }
        });
        submitPayload["disabled"] = true;
        this.$store.commit("updateSearchSubmitValues", submitPayload);
      } else if (value.includes("&")) {
        this.$store.commit("updateSearchBoxValidations", {
          [name]: {
            invalid: true,
            description: "Please remove &"
          }
        });
        submitPayload["disabled"] = true;
        this.$store.commit("updateSearchSubmitValues", submitPayload);
      } else {
        this.$store.commit("updateSearchBoxValidations", {
          [name]: {
            invalid: false,
            description: ""
          }
        });
        
        if (name === "query" && value && !this.sort.invalid) {
          submitPayload["disabled"] = false;
        } else if (name === "query" && !value) {
          submitPayload["disabled"] = true;
        }
        else if (name==='sort' && this.submit.query && !this.query.invalid){
          submitPayload["disabled"] = false;
        }
        this.$store.commit("updateSearchSubmitValues", submitPayload);
      }
    console.log(this.getSearchSubmitValues)
    },
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
        console.log(payload);
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
.label-required::after {
  content: "*";
  font-size: $font-size-m;
  color: red;
  margin-left: 0.2rem;
}

@media all and (max-width: 575px) {
  input {
    margin-left: auto;
    margin-right: auto;
  }
}

@media all and (max-width: 408px) {
  .block-content {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  select {
    max-width: 145px;
  }
}
</style>
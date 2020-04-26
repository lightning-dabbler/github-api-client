import Vue from "vue";
import Vuex from "vuex";
const { trending } = require('@/lib/trending')
const { emoji } = require('@/lib/emoji')
const { search } = require('@/lib/search')
console.log("vuex store")
Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        trending: {
            active: {
                developers: false,
                repositories: true
            },
            since: 'daily',
            headers: {},
            items: [],
            status_code: false,
            loading: {
                active: false,
                canCancel: false,
                isFullPage: false,
                color: '#000000',
                loader: 'spinner',
                width: 70,
                height: 70,
                backgroundColor: '#ffffff',
                opacity: 0.5,
                zIndex: 999,
            }
        },
        emojis: {

        },
        search: {
            searchBox: {
                order: {
                    selected: { html: "Descending", value: "desc" },
                    options: [
                        { html: "Descending", value: "desc" }, { html: "Ascending", value: "asc" }
                    ]
                },
                type: {
                    selected: { html: "Commits", value: "commits" },
                    options: [
                        { html: "Commits", value: "commits" }, { html: "Repositories", value: "repositories" }, { html: "Users", value: "users" }
                    ]
                },
                query: {
                    invalid: false,
                    message: ""
                },
                sort: {
                    invalid: false,
                    message: ""
                },
                loading: {
                    active: false,
                    canCancel: false,
                    isFullPage: false,
                    color: '#000000',
                    width: 70,
                    height: 70,
                    backgroundColor: '#ffffff',
                    opacity: 0.5,
                    zIndex: 999,
                }
            },
            submit: {
                disabled: true,
                query: "",
                sort: ""
            }
        }
    },
    getters: {
        getTrendingFlags: state => {
            console.log('Getter: getTrendingFlags Started')
            return state.trending
        },
        getEmoji: state => (name) => {
            console.log('Getter: getEmoji Started')
            const result = {}
            result[name] = state.emojis[name]
            console.log(`Getter: getEmoji retrieving ${JSON.stringify(result)}`)
            return result
        },
        getTrendingLoader: state => {
            console.log('Getter: getTrendingLoader Started')
            const loadingData = state.trending.loading
            console.log(`Getter: getTrendingLoader retrieving ${JSON.stringify(loadingData)}`)
            return loadingData
        },
        getSearchBoxSelect: state => {
            console.log('Getter: getSearchBoxSelect Started')
            const orderSelected = state.search.searchBox.order.selected
            const typeSelected = state.search.searchBox.type.selected
            const searchBoxSelect = { order: { selected: orderSelected }, type: { selected: typeSelected } }
            const typeOptionsLeftover = []
            const orderOptionsLeftover = []
            for (const i of state.search.searchBox.order.options) {
                if (i.value !== orderSelected.value) {
                    orderOptionsLeftover.push(i)
                }
            }
            for (const j of state.search.searchBox.type.options) {
                if (j.value !== typeSelected.value) {
                    typeOptionsLeftover.push(j)
                }
            }
            searchBoxSelect.order.options = orderOptionsLeftover
            searchBoxSelect.type.options = typeOptionsLeftover
            console.log(`Getter: getSearchBoxSelect retrieving ${JSON.stringify(searchBoxSelect)}`)
            return searchBoxSelect
        },
        getSearchBoxValidations: state => {
            console.log('Getter: getSearchBoxValidations Started')
            const validations = { query_validation: state.search.searchBox.query, sort_validation: state.search.searchBox.sort }
            console.log(`Getter: getSearchBoxValidations retrieving ${JSON.stringify(validations)}`)
            return validations
        },
        getSearchSubmitValues: state => {
            console.log('Getter: getSearchSubmitValues Started')
            const submit = state.search.submit
            console.log(`Getter: getSearchSubmitValues retrieving ${JSON.stringify(submit)}`)
            return submit
        },
        getSearchBoxLoader: state => {
            console.log('Getter: getSearchLoader Started')
            const loadingData = state.search.searchBox.loading
            console.log(`Getter: getSearchLoader retrieving ${JSON.stringify(loadingData)}`)
            return loadingData
        },
        getSearchPayload: state => {
            console.log('Getter: getSearchPayload Started')
            const submit = state.search.payload
            console.log(`Getter: getSearchPayload retrieving ${JSON.stringify(submit)}`)
            return submit
        }
    },
    mutations: {
        updateTrendingFlags(state, payload) {
            /**
             * @param {Object} payload 
             */
            console.log("Mutation: updateTrendingFlags Started")
            if (payload.active) {
                Vue.set(state.trending.active, "developers", payload.active.developers)
                Vue.set(state.trending.active, "repositories", payload.active.repositories)
            }
            if (payload.since) {
                Vue.set(state.trending, "since", payload.since)
            }
            if (payload.results) {
                Vue.set(state.trending, "items", payload.results.items)
                Vue.set(state.trending, "headers", payload.results.headers)
                Vue.set(state.trending, "status_code", payload.results.status_code)
            }
            console.log(state.trending.active, `since ${state.trending.since}`)
            console.log("Mutation: updateTrendingFlags Complete")
        },
        updateEmojis(state, payload) {
            /**
             * @param {Object} payload 
             */
            console.log("Mutation: updateEmojis Started")
            Vue.set(state.emojis, payload.name, payload.exists ? payload.img : '/static/images/error.svg')
            console.log("Mutation: updateEmojis Complete")
        },
        updateTrendingLoader(state, payload) {
            /**
             * @param {boolean} payload
             */
            console.log("Mutation: updateTrendingLoader Started")
            Vue.set(state.trending.loading, 'active', payload)
            console.log("Mutation: updateTrendingLoader Complete")
        },
        updateSearchBox(state, payload) {
            /**
             * @param {Object} payload
             */
            console.log("Mutation: updateSearchBox Started")
            if (payload.order) {
                Vue.set(state.search.searchBox.order, 'selected', payload.order.selected)
            }
            if (payload.type) {
                Vue.set(state.search.searchBox.type, 'selected', payload.type.selected)
            }
            console.log("Mutation: updateSearchBox Complete")
        },
        updateSearchBoxValidations(state, payload) {
            /**
             * @param {Object} payload
             */
            console.log("Mutation: updateSearchBoxValidations Started")
            if (payload.query) {
                Vue.set(state.search.searchBox.query, 'invalid', payload.query.invalid)
                Vue.set(state.search.searchBox.query, 'message', payload.query.message)
            }
            if (payload.sort) {
                Vue.set(state.search.searchBox.sort, 'invalid', payload.sort.invalid)
                Vue.set(state.search.searchBox.sort, 'message', payload.sort.message)
            }
            console.log("Mutation: updateSearchBoxValidations Complete")
        },
        updateSearchSubmitValues(state, payload) {
            /**
             * @param {Object} payload
             */
            console.log("Mutation: updateSearchSubmitValues Started")
            if (payload.disabled === true || payload.disabled === false) {
                Vue.set(state.search.submit, 'disabled', payload.disabled)
            }
            if (payload.query || payload.query === '') {
                Vue.set(state.search.submit, 'query', payload.query)
            }
            if (payload.sort || payload.sort === '') {
                Vue.set(state.search.submit, 'sort', payload.sort)
            }
            console.log("Mutation: updateSearchSubmitValues Complete")
        },
        updateSearchBoxLoader(state, payload) {
            /**
             * @param {boolean} payload
             */
            console.log("Mutation: updateSearchBoxLoader Started")
            Vue.set(state.search.searchBox.loading, 'active', payload)
            console.log("Mutation: updateSearchBoxLoader Complete")
        },
        setSearchPayload(state, payload) {
            /**
             * @param {Object} payload
             */
            console.log("Mutation: setSearchPayload Started")
            Vue.set(state.search, 'payload', payload)
            if (payload.length < 100) {
                Vue.set(state.search.payload, 'load_more', false)
            }
            else {
                Vue.set(state.search.payload, 'load_more', true)
            }
            console.log("Mutation: setSearchPayload Complete")
        },
        removeSearchPayload(state, payload) {
            /**
             * @param {boolean} payload
             */
            console.log("Mutation: removeSearchPayload Started")
            if (payload && state.search.payload) {
                Vue.delete(state.search, 'payload')
                console.log('state.search.payload object removed')
            }
            console.log("Mutation: removeSearchPayload Complete")
        },
        incrementPage: state => {
            console.log("Mutation: incrementPage Started")
            state.search.payload.args.page++
            console.log("New params:", state.search.payload.endpoint, state.search.payload.query, state.search.payload.args)
            console.log("Mutation: incrementPage Complete")
        },
        extendSearchPayload(state, payload) {
            /**
             * @param {Object} payload
             */
            console.log("Mutation: extendSearchPayload Started")
            if (payload.items.length < 100) {
                Vue.set(state.search.payload, 'load_more', false)
            }
            else {
                Vue.set(state.search.payload, 'load_more', true)
            }
            state.search.payload.items.push(...payload.items)
            Vue.set(state.search.payload, "headers", payload.headers)
            Vue.set(state.search.payload, "status_code", payload.status_code)
            Vue.set(state.search.payload, "length", state.search.payload.items.length)
            console.log("Mutation: extendSearchPayload Complete")
        }
    },
    actions: {
        callTrending: async function callTrending(context, payload) {
            /**
             * @param {Object} payload 
             */
            console.log("Action: callTrending Started")
            const data = await trending(payload)
            console.log(data)
            payload.results = data
            context.commit("updateTrendingFlags", payload)
            console.log("Action: callTrending Complete")
        },
        callGetEmoji: async function callGetEmoji(context, payload) {
            /**
             * @param {String} payload 
             */
            console.log("Action: callGetEmojis Started")
            const data = await emoji(payload)
            console.log(data)
            context.commit("updateEmojis", data)
            console.log("Action: callGetEmoji Complete")
        },
        callSearch: async function callSearch(context, payload) {
            /**
             * @param {object} payload 
             */
            console.log("Action: callSearch Started")
            if (context.state.search.payload) {
                console.log("Loading More data")
                context.commit("incrementPage")
                const data = await search(context.state.search.payload.endpoint,
                    context.state.search.payload.query,
                    context.state.search.payload.args)
                console.log(data)
                context.commit("extendSearchPayload", data)
            }
            else {
                console.log("'payload' not in state.search")
                const data = await search(payload.endpoint, payload.query, payload.args)
                Vue.set(payload, "items", data.items)
                Vue.set(payload, "headers", data.headers)
                Vue.set(payload, "status_code", data.status_code)
                Vue.set(payload, "length", data.items.length)
                context.commit("setSearchPayload", payload)
            }
            console.log("Action: callSearch Complete")
        }
    }
});
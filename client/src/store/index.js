import Vue from "vue";
import Vuex from "vuex";
const { trending } = require('@/lib/trending')
const { emoji } = require('@/lib/emoji')
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
                }
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
        getSearchBox: state => {
            console.log('Getter: getSearchBox Started')
            const orderSelected = state.search.searchBox.order.selected
            const typeSelected = state.search.searchBox.type.selected
            const searchBox = {order:{selected:orderSelected},type:{selected:typeSelected}}
            const typeOptionsLeftover = []
            const orderOptionsLeftover = []
            for (const i of state.search.searchBox.order.options){
                if(i.value !== orderSelected.value){
                    orderOptionsLeftover.push(i)
                }
            }
            for (const j of state.search.searchBox.type.options){
                if(j.value !== typeSelected.value){
                    typeOptionsLeftover.push(j)
                }
            }
            searchBox.order.options = orderOptionsLeftover
            searchBox.type.options = typeOptionsLeftover
            console.log(`Getter: getSearchBox retrieving ${JSON.stringify(searchBox)}`)
            return searchBox
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
        updateSearchBox(state,payload){
            /**
             * @param {Object} payload
             */
            console.log("Mutation: updateSearchBox Started")
            if (payload.order){
                Vue.set(state.search.searchBox.order,'selected',payload.order.selected)
            }
            if (payload.type){
                Vue.set(state.search.searchBox.type,'selected',payload.type.selected)
            }
            console.log("Mutation: updateSearchBox Complete")
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
        }
    }
});
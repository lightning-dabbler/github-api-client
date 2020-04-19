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
            results: {},
            loading: {
                active: false,
                canCancel: false,
                isFullPage: false,
                color: '#000000',
                loader: 'spinner',
                width: 64,
                height: 64,
                backgroundColor: '#ffffff',
                opacity: 0.5,
                zIndex: 999,
            }
        },
        emojis: {

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
            Vue.set(state.trending, "since", payload.since ? payload.since : state.trending.since)
            Vue.set(state.trending, "results", payload.results ? payload.results : state.trending.results)
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
        updateTrendingLoader(state,payload){
            /**
             * @param {boolean} payload
             */
            console.log("Mutation: updateTrendingLoader Started")
            Vue.set(state.trending.loading,'active',payload)
            console.log("Mutation: updateTrendingLoader Complete")
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
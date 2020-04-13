import Vue from "vue";
import Vuex from "vuex";
const { trending } = require('@/lib/trending')

Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        trending: {
            developers: false,
            since: daily,
            results: {}
        }
    },
    getters: {
        getTrendingFlags: state => {
            console.log('Getter: getTrendingFlags Started')
            return state.trending
        }

    },
    mutations: {
        updateTrendingFlags(state, payload) {
            console.log("Mutation: updateTrendingFlags Started")
            state.trending.developers = payload.developers !== state.trending.developers ? payload.developers : state.trending.developers
            state.trending.since = payload.since ? payload.since : state.trending.since
            state.trending.results = payload.results ? payload.results : state.trending.results
            console.log("Mutation: updateTrendingFlags Complete")
        }
    },
    actions: {
        callTrending: async function callTrending(context,payload){
            console.log("Action: callTrending Started")
            const data = await trending(payload)
            payload.results = data
            context.commit("updateTrendingFlags",payload)
            console.log("Action: callTrending Complete")
        }
    }
});
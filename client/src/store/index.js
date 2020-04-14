import Vue from "vue";
import Vuex from "vuex";
const { trending } = require('@/lib/trending')
const { emoji } = require('@/lib/emoji')
console.log("vuex store")
Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        trending: {
            active:{
                developers:false,
                repositories:true
            },
            since: 'daily',
            results: {}
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
        }
    },
    mutations: {
        updateTrendingFlags(state, payload) {
            /**
             * @param {Object} payload 
             */
            console.log("Mutation: updateTrendingFlags Started")
            if (payload.active){
                Vue.set(state.trending.active,"developers", payload.active.developers)
                Vue.set(state.trending.active,"repositories", payload.active.repositories)
            }
            Vue.set(state.trending,"since", payload.since ? payload.since : state.trending.since)
            Vue.set(state.trending,"results", payload.results ? payload.results : state.trending.results)
            console.log(state.trending.active,`since ${state.trending.since}`)
            console.log("Mutation: updateTrendingFlags Complete")
        },
        updateEmojis(state, payload) {
            /**
             * @param {Object} payload 
             */
            console.log("Mutation: updateEmojis Started")
            Vue.set(state.emojis,payload.name, payload.exists ? payload.img : false)
            console.log("Mutation: updateEmojis Complete")
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
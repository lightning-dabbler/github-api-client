import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'static/css/global.css'
import VueRouter from 'vue-router'
import Vue from 'vue'
import VueLazyLoad from 'vue-lazyload'
import App from './App.vue'
import { routes } from './routes'
import store from '@/store'

Vue.use(VueLazyLoad)
Vue.use(VueRouter)

const router = new VueRouter({
    routes,
    mode: 'history'
    // ,
    // scrollBehavior(to, from, savePosition) {
    //     if (savePosition) {
    //         return savePosition
    //     }
    //     else {
    //         return { x: 0, y: 0 }
    //     }
    // }
})

router.beforeEach((to, from, next) => {
    if (to.meta.title) {
        document.title = to.meta.title
    }
    next()
})

new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App)
})
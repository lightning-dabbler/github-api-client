console.info('routes.js')

const titles = {
    home: 'GitHub API - OI',
    search: 'Search - GitHub API',
    notFound: '404 - NOT FOUND'
}


const Home = () =>  import('views/HomePage.vue')
const Search = () =>  import('views/SearchPage.vue')
const NotFound = () => import('views/NotFoundPage.vue')

export const routes = [
    {
        path: '/',
        name: 'landing',
        component: Home,
        meta: {
            title: titles.home
        }
    },
    {
        path: '/home',
        name: 'home',
        component: Home,
        meta: {
            title: titles.home
        }
    },
    {
        path: '/search',
        name: 'search',
        component: Search,
        meta: {
            title: titles.search
        }
    },
    {
        path: '*', 
        component: NotFound,
        meta: {
            title: titles.notFound
        }
    }

]
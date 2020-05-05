console.info('routes.js')

const titles = {
    home: 'GitHub API - OI',
    search: 'Search - GitHub API',
    notFound: '404 - NOT FOUND'
}

// resolve|require bc some components are using combinations of
// require and export

const Home = resolve => require(['views/HomePage.vue'], m => resolve(m.default));  

const Search = resolve => require(['views/SearchPage.vue'], m => resolve(m.default));
const NotFound = resolve => require(['views/NotFoundPage.vue'], m => resolve(m.default));

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
const { search } = require('../src/lib/search')



async function testSearch() {
    var x
    x = await search('repositories', 'stars:>1+forks:>1', {per_page:100, page:2, sort:'stars+forks', order:'desc'})
    console.log(typeof x)
    x = await search('users','lightn',{})
    console.log(typeof x)
    x = await search('commits','test+repo:vuejs/vue',{per_page:100,page:1})
    console.log(typeof x)
}

testSearch()



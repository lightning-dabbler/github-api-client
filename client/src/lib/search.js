const { retrieveInternalAPIData } = require('./utils')
require('../../lib/config')
const api = process.env.API_URL

async function search(endpoint, query, {per_page, page, sort, order}) {
    /** 
    * Fetches search data from internal API
    * @param {string} endpoint
    * @param {string} query 
    * @param {number|undefined} per_page
    * @param {number|undefined} page 
    * @param {string|undefined} sort  
    * @param {string|undefined} order
    * @return {object}
    */

    console.log('Function: search')
    page = page ? page : 1
    per_page = per_page ? per_page : 100

    const params = { endpoint, query, per_page, page, sort, order }

    console.log(`Parameters = ${JSON.stringify(params)}`)

    var uri = `${api}/api/search/${endpoint}/${query}?page=${page}&${per_page}`
    if (sort) uri = `${uri}&sort=${sort}`
    if (order) uri = `${uri}&order=${order}`

    const data = await retrieveInternalAPIData(uri)
    console.log(`Search ${endpoint}:: ${data.items ? `${data.items.length} items returned` : `ERR NO DATA Trending @ uri ${uri}`}`)
    return data

}

module.exports = {
    search
}
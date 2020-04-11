const { retrieveInternalAPIData } = require('./utils')
require('../../lib/config')
const api = process.env.API_URL

async function trending({developers,since,refresh}) {
    /** 
   * Fetches Trending repositories/developers data from internal API 
   * @params {boolean|undefined} developers
   * @params {string|undefined} since
   * @params {boolean|undefined} refresh
   * @return {object}
   */

    console.log('Function: trending')

    developers = developers === true ? developers : false
    since = ['daily', 'weekly', 'monthly'].includes(since) ? since : undefined
    refresh = refresh === true ? refresh : false

    const params = { developers, since, refresh }
    console.log(`Parameters = ${JSON.stringify(params)}`)

    var uri = `${api}/api/cached/trending`
    

    if (developers && since) {
        uri = `${uri}?developers=${developers}&since=${since}`
        if(refresh) uri = `${uri}&refresh=${true}`
    }
    else if (developers) {
        uri = `${uri}?developers=${developers}`
        if(refresh) uri = `${uri}&refresh=${true}`
    }
    else if (since) {
        uri = `${uri}?&since=${since}`
        if(refresh) uri = `${uri}&refresh=${true}`
    }
    else{
        if(refresh) uri = `${uri}?&refresh=${true}`
    }

    const data = await retrieveInternalAPIData(uri)
    console.log(`Trending:: ${data.items ? `${data.items.length} items returned` : `ERR NO DATA Trending @ uri ${uri}`}`)
    return data
}

module.exports = {
    trending
}

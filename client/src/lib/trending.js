const config = require('../../lib/config')
const { keyExists, getKey, retrieveInternalAPIData } = require('../src/lib/utils')

const api = config.api_url

async function trending(endpoint, key, developers, since, refresh) {
    /** 
   * Fetches Trending repositories/developers data from internal api or redis client
   * @params {string} endpoint
   * @params {string} key
   * @params {boolean|undefined} developers
   * @params {string|undefined} since
   * @params {boolean|undefined} refresh
   * @return {object}
   */
    developers = developers === true ? developers : false
    since = ['daily', 'weekly', 'monthly'].includes(since) ? since : undefined
    refresh === true ? developers : false
    var uri = `${api}${endpoint}`
    
    if (developers && since) {
        uri = `${uri}?developers=${developers}&since=${since}`
    }
    else if (developers) {
        uri = `${uri}?developers=${developers}`
    }
    else if (since) {
        uri = `${uri}?&since=${since}`
    }

    if (keyExists(key) && !refresh) {
        const data = await getKey(key, uri)
    }
    else {
        const data = await retrieveInternalAPIData(key, uri, `${seconds}`)
    }
    return data
}

module.exports = {
    trending
}

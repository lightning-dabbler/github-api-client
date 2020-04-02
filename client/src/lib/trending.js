const config = require('../../lib/config')
const { keyExists, getKey, retrieveInternalAPIData } = require('./utils')

const api = config.api_url

async function trending(endpoint, key, seconds, developers, since, refresh) {
    /** 
   * Fetches Trending repositories/developers data from internal API or Redis client
   * @params {string} endpoint
   * @params {string} key
   * @params {number} seconds
   * @params {boolean|undefined} developers
   * @params {string|undefined} since
   * @params {boolean|undefined} refresh
   * @return {object}
   */

    console.log('Function: trending')

    developers = developers === true ? developers : false
    since = ['daily', 'weekly', 'monthly'].includes(since) ? since : undefined
    refresh = refresh === true ? refresh : false

    const params = { endpoint, key, seconds, developers, since, refresh }
    console.log(`Parameters = ${JSON.stringify(params)}`)

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
    console.log(`uri = ${uri}`)

    const keyInRedisClient = await keyExists(key)
    if (keyInRedisClient && !refresh) {
        const data = await getKey(key, uri)
        return data
    }
    else {
        const data = await retrieveInternalAPIData(key, uri, `${seconds}`)
        return data
    }
}

module.exports = {
    trending
}

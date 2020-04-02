const config = require('../../lib/config')
const { keyExists, getKey, retrieveInternalAPIData } = require('./utils')

const api = config.api_url

async function emoji(endpoint, emoji, seconds) {
    /**
     * Fetches image url associated with emoji from internal
     * API or Redis client
     * @params {string} endpoint
     * @params {string} emoji
     * @seconds {number} seconds
     * @return {object}
     */
    console.log('Function: emoji')

    const uri = `${api}${endpoint}?emoji=${emoji}`
    console.log(uri)

    const params = { endpoint, emoji, seconds }
    console.log(`Parameters = ${JSON.stringify(params)}`)

    keyInRedisClient = await keyExists(emoji)
    if (keyInRedisClient) {
        const data = await getKey(emoji, uri)
        if (data.hasOwnProperty(`${emoji}`)) {
            return { exists: true, img: data[`${emoji}`] }
        }
        else {
            return { exists: false }
        }
    }
    else {
        const data = await retrieveInternalAPIData(emoji, uri, `${seconds}`)
        if (data.hasOwnProperty(`${emoji}`)) {
            return { exists: true, img: data[`${emoji}`] }
        }
        else {
            return { exists: false }
        }
    }
}

module.exports = {
    emoji
}

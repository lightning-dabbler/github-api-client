const { retrieveInternalAPIData } = require('./utils')
require('../../lib/config')
const api = process.env.API_URL

async function emoji(emoji) {
    /**
     * Fetches image url data associated with emoji from internal API
     * @params {string} emoji
     * @return {object}
     */
    console.log('Function: emoji')

    const uri = `${api}/cached/emojis/${emoji}`
    console.log(uri)

    console.log(`Fetching emoji data for ${emoji}; ${uri}`)
    const data = await retrieveInternalAPIData(uri)
    console.log(`emoji data = ${JSON.stringify(data)}`)
    return data
}

module.exports = {
    emoji
}

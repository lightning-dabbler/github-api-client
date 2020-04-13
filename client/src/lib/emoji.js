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

    const uri = `${api}/api/cached/emojis/${emoji}`
    console.log(uri)

    console.log(`Fetching emoji data for ${emoji}; ${uri}`)
    const data = await retrieveInternalAPIData(uri)
    console.log(`emoji data = ${JSON.stringify(data)}`)
    return data
}


const getEmoji = async (key) => {
    /**
     * Used In Components fetches image associated with key
     * @params {string} key
     * @return {object}
     */
    const result = {};
    var data = await emoji(key);
    result[key] = data.exists ? data.img : undefined;
    console.log(`emojis = ${JSON.stringify(result)}`);
    return result;
  }

module.exports = {
    emoji, getEmoji
}

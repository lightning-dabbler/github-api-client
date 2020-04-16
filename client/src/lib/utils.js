const axios = require('axios')

/********* INTERNAL API **********/
async function retrieveInternalAPIData(uri) {
  /** 
   * Retrieves data from Internal API at uri 
   * @param {string} uri
   * @return {object}
   */
  console.log('Function: retrieveInternalAPIData')
  return axios.get(uri)
    .then(res => {
      const data = res.data
      console.log(`Success - function: retrieveInternalAPIData --> REQUEST TO INTERNAL API ${uri} \nCOMPLETE ! STATUS CODE: ${res.status} ${res.statusText}`)
      return data

    })
    .catch(error => {
      console.error(`Failure - function: retrieveInternalAPIData --> REQUEST TO INTERNAL API ${uri}\n`, error.response ? error.response : 'NO RESPONSE');
      console.error(error)
      return {}
    })
}

module.exports = {
  retrieveInternalAPIData
}


const client = require('../../lib/redis-client')
const axios = require('axios')

/********** REDIS *********/
async function setKeyExpiration(key, seconds) {
  /** 
 * Sets data at key within Redis client
 * @params {string} key
 * @params {string} seconds
 * @return {undefined}
 */

  client.expireAsync(key, seconds).then(res => {
    console.log(`Success - function: setKeyExpiration --> EXPIRATION FOR KEY "${key}" SET at ${seconds} secs; RESPONSE = ${res}`)
  }).catch(err => {
    console.error('Failure - function: setKeyExpiration --> NO EXPIRATION SET FOR KEY "${key}"', err)
  })
}

async function setKey(key, data, seconds) {
  /** 
   * Sets data at key within Redis client
   * @params {string} key
   * @params {object} data
   * @params {string} seconds
   * @return {undefined}
   */

  client.setAsync(key, JSON.stringify(data)).then(async res => {
    console.log(`Success - function: setKey --> Data set at Key; Response = ${res}`)
    await setKeyExpiration(key, seconds)
  }).catch(err => {
    console.error('Failure - function: setKey --> DATA NOT SET !\n', err)
  })
}

async function getKey(key, uri) {
  /** 
   * Retrieves data from Redis client at given key. If not exists,
   * then retrieve data from internal API at URI 
   * @params {string} key
   * @params {string} uri
   * @return {object}
   */

  return client.getAsync(key).then(data => {
    console.log('Success - function: getKey --> KEY INDEXED')
    return JSON.parse(data)
  }).catch(async err => {
    console.error('Failure - function: getKey --> NO KEY TO INDEX !\n', err)
    const data = await retrieveInternalAPIData(uri)
    return data
  })
}

async function keyExists(key) {
  /** 
   * Checks for the existence of key in Redit Client cache 
   * @params {string} key
   * @return {number}
   */

  return client.existsAsync(key).then(res => {
    console.log(`Success - function: keyExists --> RESPONSE = ${res}`)
    return res
  }).catch(err => {
    console.error('Failure - function: keyExists --> ERROR\n', err)
    return 0
  })
}

async function flushdb() {
  client.flushdbAsync().then(res => {
    console.log(`Success - function: flushdb --> RESPONSE = ${res}`)
  }).catch(err => {
    console.error('Failure - function: flushdb --> ERROR\n', err)
  })
}

async function quitConn() {
  client.quitAsync().then(res => {
    console.log(`Success - function: quitConn --> RESPONSE = ${res}\nCONNECTION OFF`)
  }).catch(err => {
    console.error('Success - function: quitConn --> ERROR\n',err)
    client.end(false)
  })
}

/********* INTERNAL API **********/
async function retrieveInternalAPIData(key, uri, seconds) {
  /** 
   * Retrieves data from Internal API at uri 
   * @params {string} key
   * @params {string} uri
   * @params {string} seconds
   * @return {object}
   */
  return axios.get(uri)
    .then(async (res) => {
      const data = res.data
      console.log(`Success - function: retrieveInternalAPIData --> REQUEST TO INTERNAL API COMPLETE ! STATUS CODE: ${data.status_code}`)
      await setKey(key, data, seconds)
      return data

    })
    .catch((error) => {
      console.error('Failure - function: retrieveInternalAPIData', error.response ? error.response : 'NO RESPONSE');
      return {}
    })
}

module.exports = {
  keyExists,
  getKey,
  retrieveInternalAPIData,
  flushdb,
  quitConn
}


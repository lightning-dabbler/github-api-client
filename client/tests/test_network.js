const client = require('../lib/redis-client')
const config = require('../lib/config')
const apiPath = `${config.api_url}/api/trending`
const axios = require('axios')

let response = {}

async function expireKey(key, seconds) {
  client.expireAsync(key, seconds).then(res => {
    console.log(`EXPIRATION FOR KEY "${key}" @ ${seconds}: ${res}`)
  }).catch(err => {
    console.error(err)
  })
}

async function quitConnection() {
  client.quitAsync().then(result => {
    console.log(`${result}: CONNECTION OFF`)
  }).catch(error => {
    console.error(error)
    client.end(false)
  })
}

async function redisDel(key) {
  client.delAsync(key).then(done => {
    console.log(`KEY REMOVED ${done}`)
  }).catch(err => {
    console.error(err)
  })
}

async function redisSet(key, data) {
  client.setAsync(key, JSON.stringify(data)).then(res => {
    console.log(`${res}: DATA SET`)
  }).catch(err => {
    console.error('NO DATA SET')
    console.error(err)
  })
}

async function redisGet(key) {
  return client.getAsync(key).then(data => {
    console.log('DATA FROM REDIS')
    return data
  }).catch(error => {
    console.error('NO DATA QUERIED')
    console.error(error)
    return {}
  })
}

async function getFromAPI(apiPath) {
  return axios.get(apiPath)
    .then((res) => {
      const data = res.data

      console.log(`REQUEST COMPLETE ! STATUS CODE: ${data.status_code}`)
      return data

    })
    .catch((error) => {
      console.error(error);
      return {}
    })
}

async function keyExists(key) {
  return client.existsAsync(key).then(res => {
    console.log(res)
    return res
  }).catch(err => {
    console.error(err)
    return false
  })
}

async function testTrendFetch(apiPath, key) {
  const exists = await keyExists(key)

  if (exists) {
    const data = await redisGet(key)
    await redisDel(key)
    await quitConnection()
    return JSON.parse(data)
  }
  else {
    const data = await getFromAPI(apiPath)
    await redisSet(key, data)
    await quitConnection()
    return data
  }
}
async function results(response, apiPath, key) {
  response.data = await testTrendFetch(apiPath, key)
  console.log(response)
}
results(response, apiPath, 'trending_repo_daily')

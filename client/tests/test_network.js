const axios = require('axios')
const redis = require('redis')
const { promisify } = require('util')

const client = redis.createClient(process.env.REDIS_URL_NET)
const apiPath = `${process.env.GITHUB_API_NET}/api/trending`

const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)
const keysAsync = promisify(client.keys).bind(client)
const delAsync = promisify(client.del).bind(client)
const quitAsync = promisify(client.quit).bind(client)

let response = {}
async function quitConnection(){
  quitAsync().then(result => {
    console.log(`${result}: CONNECTION OFF`)
  }).catch(error => {
    console.error(error)
    client.end(false)
  })
}

async function redisDel(key){
  delAsync(key).then(done => {
    console.log(`KEY REMOVED ${done}`)
  }).catch(err =>{
    console.error(err)
  })
}

async function redisSet(key,data){
  setAsync(key,JSON.stringify(data)).then(res =>{
    console.log(`${res}: DATA SET`)
  }).catch(err => {
    console.error('NO DATA SET')
    console.error(err)
  })
}

async function redisGet(key) {
  return getAsync(key).then(data => {
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
      // console.log(data.items[0].built_by)
      return data

    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
      return {}
    })
}

async function queryKeys(pattern){
  return keysAsync(pattern).then(results => {
    console.log(results, typeof results)
    return results
  }).catch(error => {
    console.error(error)
    return []
  })
}
async function testTrendFetch(apiPath, key) {
  const keys = await queryKeys('trending*')

  if (keys.includes(key)) {
    const data = await redisGet(key)
    await redisDel(key)
    await quitConnection()
    return JSON.parse(data)
  }
  else {
    const data = await getFromAPI(apiPath)
    await redisSet(key,data)
    await quitConnection()
    return data 
  }
}
async function results(response, apiPath,key) {
  response.data = await testTrendFetch(apiPath, key)
  console.log(response)
}
results(response, apiPath,'trending_repo_daily')

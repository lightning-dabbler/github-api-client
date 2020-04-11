const redis = require('redis')
const { promisify } = require('util')
const redis_url = process.env.REDIS_URL_NET
const client = redis.createClient(redis_url)
console.log(redis_url)

const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)
const delAsync = promisify(client.del).bind(client)
const quitAsync = promisify(client.quit).bind(client)
const existsAsync = promisify(client.exists).bind(client)
const expireAsync = promisify(client.expire).bind(client)
const flushdbAsync = promisify(client.flushdb).bind(client)

module.exports = {
    ...client,
    getAsync,
    setAsync,
    delAsync,
    quitAsync,
    existsAsync,
    expireAsync,
    flushdbAsync
}
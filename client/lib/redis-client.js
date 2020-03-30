const redis = require('redis')
const { promisify } = require('util')
const Config = require('./config')
const client = redis.createClient(Config.redis_url)
console.log(Config.redis_url)

const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)
const delAsync = promisify(client.del).bind(client)
const quitAsync = promisify(client.quit).bind(client)
const existsAsync = promisify(client.exists).bind(client)
const expireAsync = promisify(client.expire).bind(client)

module.exports = {
    ...client,
    getAsync,
    setAsync,
    delAsync,
    quitAsync,
    existsAsync,
    expireAsync
}
const redis = require('redis')
const { delay } = require('./lib/utils')

async function pingRedisAPI(retry, milliseconds, redis_url) {
    let attempts = 0
    let status = 0
    let client
    while (status !== 200 && attempts < retry) {
        console.log(`Attempting Request #${attempts + 1}`)
        status = 200
        client = redis.createClient(`${redis_url}`)
        client.on("error", err => {
            console.log(err)
            status = 404
        })
        client.quit((err, res) => {
            if (err) {
                console.log(err)
                client.end(false)
            }
            else {
                console.log(res)
            }
        })
        await delay(milliseconds)
        attempts += 1
    }
    if (status === 200) {
        console.info(`Successful - Ping to Redis API: ${redis_url}`)
    }
    else {
        throw new Error(`Failure - Ping to Redis API: ${redis_url}`)
    }
}

pingRedisAPI(5, 5000, process.env.REDIS_URL_NET)
    .catch(err => {
        console.error(err)
        process.exit(1)
    })


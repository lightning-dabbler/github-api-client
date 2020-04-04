const { keyExists, flushdb, quitConn } = require('../src/lib/utils')
const { delay } = require('../lib/utils')
const { trending } = require('../src/lib/trending')



async function testTrending() {
    var x
    await flushdb()
    x = await trending('/api/trending', 'trending_repo_daily', 30)
    console.log(typeof x)
    x = await trending('/api/trending', 'trending_dev_monthly', 30, developers = true, since = 'monthly')
    console.log(typeof x)
    await delay(25000)
    x = await trending('/api/trending', 'trending_repo_daily', 20)
    console.log(typeof x)
    await delay(5000)
    x = await trending('/api/trending', 'trending_dev_monthly', 30)
    console.log(typeof x)
    x = await trending('/api/trending', 'trending_repo_daily', 20)
    console.log(typeof x)
    await flushdb()
    var y = await keyExists('trending_repo_daily')
    y = await keyExists('trending_dev_monthly')
    await quitConn()
}

testTrending()



const { keyExists,flushdb,quitConn,delay } = require('../src/lib/utils')
const { emoji } = require('../src/lib/emoji')



async function testEmoji() {
    var x
    await flushdb()
    x = await emoji('/api/emojis', '-1', 30)
    console.log(x)
    x = await emoji('/api/emojis', 'octocat', 30)
    console.log(x)
    await delay(25000)
    x = await emoji('/api/emojis', '-1', 20)
    console.log(x)
    await delay(5000)
    x = await emoji('/api/emojis', 'octocat', 30)
    console.log(x)
    x = await emoji('/api/emojis', 'djbkfdbk', 20)
    console.log(x)
    await flushdb()
    var y = await keyExists('-1')
    y = await keyExists('emoji_dev_monthly')
    await quitConn()
}

testEmoji()



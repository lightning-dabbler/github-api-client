const { emoji } = require('../src/lib/emoji')



async function testEmoji() {
    var x
    x = await emoji('octocat')
    console.log(x)
    x = await emoji('lightning')
    console.log(x)
}

testEmoji()



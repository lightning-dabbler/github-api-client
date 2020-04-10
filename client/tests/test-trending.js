const { trending } = require('../src/lib/trending')



async function testTrending() {
    var x
    x = await trending({refresh:true}) 
    console.log(typeof x)
    x = await trending({})
    console.log(typeof x)
    x = await trending({developers:true,since:'monthly'})
    console.log(typeof x)
}

testTrending()


// Parameters = {"developers":true,"refresh":false}
// Function: retrieveInternalAPIData
// Failure - function: retrieveInternalAPIData --> REQUEST TO INTERNAL API http://github_api:2064/api/cached/trending?developers=true&refresh=false
//  NO RESPONSE
// Trending:: ERR NO DATA Trending @ uri http://github_api:2064/api/cached/trending?developers=true&refresh=false
// object
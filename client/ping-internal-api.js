const axios = require('axios')

async function delay(milliseconds, api_url) {

    return new Promise(resolve => {
        setTimeout(() => {
            resolve(axios.get(api_url).then(res => {
                console.log(`GET for ${api_url}; Response Status = ${res.status}`)
                return res.status
            }).catch(err => {
                console.log(`GET ERROR for ${api_url}; Response = ${err.response?err.response:'NO RESPONSE'}`)
                return 404
            })
            )
        }, milliseconds)
    })
}

async function pingAPI(retry, milliseconds, api_url) {
    let attempts = 0
    let status = 0
    while (status !== 200 && attempts < retry) {
        console.log(`Attempting Request #${attempts+1}`)
        status = await delay(milliseconds, api_url)
        attempts += 1
    }
    if (status === 200) {
        console.info(`Successful - Ping to API: ${api_url}`)
    }
    else {
        throw new Error(`Failure - Ping to API: ${api_url}`)
        
    }
}

pingAPI(3, 5000, process.env.GITHUB_API_NET)
.catch(err=>{
    console.error(err)
    process.exit(1)
})


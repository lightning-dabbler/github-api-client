const axios = require('axios')

async function delay(seconds,api_url){

    return new Promise(setTimeout(()=>{
        axios.get(api_url).then(res => {
            return res.status
        }).catch(err=>{
            console.log(err)
            return 404
        })
    },seconds))
}

async function pingAPI(retry,seconds,api_url){
    const attempts = 0
    let status = 0
    while (status !== 200 && attempts < retry){
        status = await delay(seconds,api_url)
    }
    if (status===200){
        console.info(`Successful Ping to API: ${api_url}`)
    }
    else {
        console.error(`Failure Ping to API: ${api_url}`)
        assert (false)
    }
}

module.exports = {
    pingAPI
}

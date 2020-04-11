const environment = process.env.NODE_ENV

if (environment === 'prod'){
    const API_URL = process.env.GITHUB_API_WEB
    console.log(`API_URL=${API_URL}`)
}
else {
    const REDIS_URL = process.env.REDIS_URL_NET
    const API_URL = process.env.GITHUB_API_NET
    console.log(`REDIS_URL=${REDIS_URL}`)
    console.log(`API_URL=${API_URL}`)
}
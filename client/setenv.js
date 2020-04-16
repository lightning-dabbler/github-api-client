const environment = process.env.NODE_ENV

if (environment === 'prod'){
    const API_URL = process.env.WEB_URL
    console.log(`API_URL=${API_URL}/api`)
}
else {
    const API_URL = process.env.GITHUB_API_NET
    console.log(`API_URL=${API_URL}`)
}
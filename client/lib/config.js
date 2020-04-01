const environment = process.env.NODE_ENV

module.exports = {
    redis_url: environment === 'prod' ? process.env.REDIS_URL_WEB : process.env.REDIS_URL_NET,
    api_url: environment === 'prod' ? process.env.GITHUB_API_WEB : process.env.GITHUB_API_NET
}
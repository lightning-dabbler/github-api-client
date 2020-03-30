const environment = process.env.NODE_ENV

module.exports = {
    redis_url: environment === 'dev' || !environment ? process.env.REDIS_URL_NET : process.env.REDIS_URL_WEB,
    api_url: environment === 'dev' || !environment ? process.env.GITHUB_API_NET : process.env.GITHUB_API_WEB
}
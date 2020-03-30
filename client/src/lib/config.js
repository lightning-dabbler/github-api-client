module.exports = {
    redis_url: process.env.NODE_ENV === 'dev' ? process.env.REDIS_URL_NET : process.env.REDIS_URL_WEB,
    api_url: process.env.NODE_ENV === 'dev' ? process.env.GITHUB_API_NET : process.env.GITHUB_API_WEB
}
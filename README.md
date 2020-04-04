<h1 align="center">GitHub API Client</h1>

> :octocat: [GitHub REST API v3]

# Table of Contents
- [Run Containers:](#run-containers)
- [APIs](#apis)
- [API Usage Examples](#api-usage-examples)
    - [Search](#search)
        - [Repositories](#search-repositories)
        - [Users](#search-users)
        - [Commits](#search-commits)
    - [GitHub Emojis](#github-emojis)
    - [Trending](#trending)
        - [Repositories](#trending-repositories)
        - [Developers](#trending-developers)
- [Tech](#tech)
- [Author](#author)

## Run Containers:
```bash
docker-compose up
# Python Flask - localhost:5064
# Redis - localhost:6379
```

APIs
---
- [api/modules/] 
    - [emojis.py] & [search.py] utilizes [GitHub REST API v3]
    - [trending.py] scrapes data from https://github.com for trending repositories/developers

API Usage Examples
----

## Search

### Repositories <a id="search-repositories"></a>
- [Example 1a](http://localhost:5064/api/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc)
- [Example 1b](http://localhost:5064/api/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc&refresh=true)

Response
```json
{
    "headers":{
        ...
    },
    "items":[
        {
      "archive_url": "https://api.github.com/repos/freeCodeCamp/freeCodeCamp/{archive_format}{/ref}", 
      "archived": false, 
      "assignees_url": "https://api.github.com/repos/freeCodeCamp/freeCodeCamp/assignees{/user}", 
        ...
      "default_branch": "master", 
      "deployments_url": "https://api.github.com/repos/freeCodeCamp/freeCodeCamp/deployments", 
      "description": "freeCodeCamp.org's open source codebase and curriculum. Learn to code for free together with millions of people.", 
      "disabled": false, 
      ...
        },
        ...
    ],
    "status_code": 200
}
```

### Users <a id="search-users"></a>
- [Example 2a](http://localhost:5064/api/search/users/lightn?)
- [Example 2b](http://localhost:5064/api/search/users/lightn?refresh=true)

Response
```json
{
    "headers":{
        ...
    },
    "items": [
    {
      "avatar_url": "https://avatars3.githubusercontent.com/u/3190659?v=4", 
      "events_url": "https://api.github.com/users/Lightn/events{/privacy}", 
      "followers_url": "https://api.github.com/users/Lightn/followers", 
      "following_url": "https://api.github.com/users/Lightn/following{/other_user}", 
      "gists_url": "https://api.github.com/users/Lightn/gists{/gist_id}", 
      ...
    },
    ...
    ],
    "status_code": 200
}
```
### Commits <a id="search-commits"></a>
- [Example 3a](http://localhost:5064/api/search/commits/test+repo:vuejs/vue)
- [Example 3b](http://localhost:5064/api/search/commits/test+repo:vuejs/vue?refresh=true)

Response
```json
  {
      "headers":{
          ...
      },
  "items": [
    {
      "author": {
        "avatar_url": "https://avatars1.githubusercontent.com/u/17667652?v=4", 
        ...
        "login": "hareku", 
        "node_id": "MDQ6VXNlcjE3NjY3NjUy", 
        "organizations_url": "https://api.github.com/users/hareku/orgs", 
        "received_events_url": "https://api.github.com/users/hareku/received_events", 
        "repos_url": "https://api.github.com/users/hareku/repos", 
        "site_admin": false, 
        "starred_url": "https://api.github.com/users/hareku/starred{/owner}{/repo}", 
        "subscriptions_url": "https://api.github.com/users/hareku/subscriptions", 
        "type": "User", 
        "url": "https://api.github.com/users/hareku"
      }, 
      "comments_url": "https://api.github.com/repos/vuejs/vue/commits/841bb084ca288e142b1958346bb1182bf6f0a564/comments", 
      "commit": {
          ...
          }
    ...
    },
    ...
  ],
  "status_code": 200
  }
```
## GitHub Emojis
- [Example 4a](http://localhost:5064/api/emojis)

Response
```json
{
    "headers":{
        ...
    },
  "items": {
    "+1": "https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8", 
    "-1": "https://github.githubassets.com/images/icons/emoji/unicode/1f44e.png?v8", 
    "100": "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8", 
    "1234": "https://github.githubassets.com/images/icons/emoji/unicode/1f522.png?v8",
    ...
  },
  "status_code": 200
}
```

- [Example 4b](http://localhost:5064/api/emojis?emoji=octocat)

## Trending

### Repositories <a id="trending-repositories"></a>
- [Example 5a](http://localhost:5064/api/trending)
- [Example 5b](http://localhost:5064/api/trending?since=weekly)

Response
```json
{
    "headers":{
        ...
    },
  "items": [
    {
      "author": "nytimes", 
      "avatar": "https://github.com/nytimes.png", 
      "built_by": [
        {
          "avatar": "https://avatars3.githubusercontent.com/u/382862", 
          "profile": "https://github.com/albertsun", 
          "username": "albertsun"
        }, 
        {
          "avatar": "https://avatars0.githubusercontent.com/u/1675354", 
          "profile": "https://github.com/archietse", 
          "username": "archietse"
        }, 
        {
          "avatar": "https://avatars3.githubusercontent.com/u/126789", 
          "profile": "https://github.com/wmandrews", 
          "username": "wmandrews"
        }
      ], 
      "description": "An ongoing repository of data on coronavirus cases and deaths in the U.S.", 
      "forks": 970, 
      "name": "covid-19-data", 
      "present_freq_stars": "2,230 stars this week", 
      "url": "https://github.com/nytimes/covid-19-data"
    },
    ...
  ],
  "status_code": 200
}
```

### Developers <a id="trending-developers"></a>
- [Example 6a](http://localhost:5064/api/trending?developers=true)
- [Example 6b](http://localhost:5064/api/trending?developers=true&since=monthly)

Response
```json
{
    "headers":{
        ...
    },
  "items": [
    {
      "avatar": "https://avatars0.githubusercontent.com/u/317464", 
      "name": "Sa\u00fal Ibarra Corretg\u00e9", 
      "popular_repository": {
        "description": "Python interface for libuv", 
        "name": "pyuv", 
        "url": "https://github.com/saghul/pyuv"
      }, 
      "profile": "https://github.com/saghul", 
      "username": "saghul"
    },
    ...
  ],
    "status_code": 200
}
```

Tech 
------
* [flask]
* [Mamba]
* [beautifulsoup4]
* [Docker]
* [Docker-Compose]
* [Redis]

Author
--------
* Osarodion Irabor

[flask]: http://flask.pocoo.org/
[GitHub REST API v3]: https://developer.github.com/v3/
[Mamba]: https://pypi.org/project/mamba/
[Docker]: https://docs.docker.com/engine/reference/builder/#usage
[Docker-Compose]: https://docs.docker.com/compose/compose-file/
[beautifulsoup4]: https://pypi.org/project/beautifulsoup4/
[emojis.py]:./api/modules/emojis.py
[search.py]:./api/modules/search.py
[trending.py]:./api/modules/trending.py
[api/modules/]:./api/modules/
[Redis]: https://redis.io/
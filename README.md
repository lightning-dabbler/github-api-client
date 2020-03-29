<h1 align="center">GitHub API Client</h1>

> :octocat: [GitHub REST API v3]

Run Flask server:
```bash
docker-compose up
# localhost:5064
```

APIs
---
- [api/modules/] 
    - [emojis.py] & [search.py] utilizes [GitHub REST API v3]
    - [trending.py] scrapes data from https://github.com for trending repositories/developers

API Usage Examples
----
## Search 
### Repositories
- [Example 1a](http://localhost:5064/api/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc)
- [Example 1b](http://localhost:5064/api/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc&refresh=true)

### Users    
- [Example 2a](http://localhost:5064/api/search/users/lightn?)
- [Example 2b](http://localhost:5064/api/search/users/lightn?refresh=true)

### Commits
- [Example 3a](http://localhost:5064/api/search/commits/test+repo:vuejs/vue)
- [Example 3b](http://localhost:5064/api/search/commits/test+repo:vuejs/vue?refresh=true)

## GitHub Emojis
- [Example 4a](http://localhost:5064/api/emojis)
- [Example 4b](http://localhost:5064/api/emojis?emoji=octocat)

## Trending
### Repositories
- [Example 5a](http://localhost:5064/api/trending)
- [Example 5b](http://localhost:5064/api/trending?since=weekly)

### Developers
- [Example 6a](http://localhost:5064/api/trending/developers)
- [Example 6b](http://localhost:5064/api/trending/developers?since=monthly)


Tech 
------
* [flask]
* [Mamba]
* [beautifulsoup4]
* [Docker]
* [Docker-Compose]

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
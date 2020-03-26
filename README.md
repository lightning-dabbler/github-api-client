# GitHub API Client

> [GitHub REST API v3]

Run Flask server:
```bash
docker-compose up
# localhost:5064
```

APIs
---
- api/modules/ 
    - [emojis.py] & [search.py] utilizes [GitHub REST API v3]
    - [trending.py] scrapes data from https://github.com for trending repositories/developers


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
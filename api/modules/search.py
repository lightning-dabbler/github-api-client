import logging

import requests
import utils
from constants import GITHUB_API

logger = logging.getLogger(__name__)


def search_lazy(endpoint, query, sort=None, order=None, page=1, per_page=100):
    """
    `endpoint:str = 'users','repositories','commits'`

    `query:str`

    - users:
    ------
    https://developer.github.com/v3/search/#search-users
    https://help.github.com/en/github/searching-for-information-on-github/searching-users

    - repositories:
    -----
    https://developer.github.com/v3/search/#search-repositories
    https://help.github.com/en/github/searching-for-information-on-github/searching-for-repositories

    - commits:
    -----
    https://developer.github.com/v3/search/#search-commits
    https://help.github.com/en/github/searching-for-information-on-github/searching-commits

    `returns generator`
    """
    logger.info("Lazy Search Wrapper for /search endpoint")
    header = {"Content-Type": "application/json"}
    if endpoint == "repositories":
        header["Accept"] = "application/vnd.github.mercy-preview+json"
    if endpoint == "commits":
        header["Accept"] = "application/vnd.github.cloak-preview"
    url = f"{GITHUB_API}/search/{endpoint}?q={query}&per_page={per_page}"
    if sort:
        url = f"{url}&sort={sort}"
    if order:
        url = f"{url}&order={order}"

    done = False
    total_returned = 0
    while not done:
        request_url = f"{url}&page={page}"
        response = requests.request("GET", request_url, headers=header)
        headers = dict(response.headers)
        status_code = response.status_code
        response = response.json()

        if status_code != 200:
            yield status_code, [], headers
            return
        total_count = response["total_count"]
        page += 1
        results = response["items"]
        yield status_code, results, headers
        total_returned += per_page
        if total_returned >= total_count:
            done = True


def search(endpoint, query, sort=None, order=None, page=1, per_page=100, strict=False):
    """
    `endpoint:str = 'users','repositories','commits'`

    `query:str`

    - users:
    ------
    https://developer.github.com/v3/search/#search-users
    https://help.github.com/en/github/searching-for-information-on-github/searching-users

    - repositories:
    -----
    https://developer.github.com/v3/search/#search-repositories
    https://help.github.com/en/github/searching-for-information-on-github/searching-for-repositories

    - commits:
    -----
    https://developer.github.com/v3/search/#search-commits
    https://help.github.com/en/github/searching-for-information-on-github/searching-commits

    `returns tuple(status_code:int,items:list[n], headers:dict)`
    """

    logger.info("Search Wrapper for /search endpoint")
    results = []

    if not strict:
        responses = search_lazy(
            endpoint, query, sort=sort, order=order, page=page, per_page=per_page
        )
        for response in responses:
            status_code = response[0]
            items = response[1]
            headers = response[2]
            results.extend(items)
    else:
        responses = search_lazy(
            endpoint, query, sort=sort, order=order, page=page, per_page=per_page
        )
        response = next(responses)
        status_code = response[0]
        items = response[1]
        headers = response[2]
        results.extend(items)
    return status_code, results, headers

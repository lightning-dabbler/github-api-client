import os
import requests

GITHUB_API = os.getenv('GITHUB_API')


def search(endpoint,query,sort=None,order=None,page=1,per_page=100,strict=False):
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
    """
    header = {'Content-Type': 'application/json'}
    url = f'{GITHUB_API}/search/{endpoint}?q={query}&per_page={per_page}'
    if sort:
        url = f'{url}&sort={sort}'
    if order:
        url = f'{url}&order={order}'
    
    results =[]
    if not strict:
        done = False
        total_returned = 0
        while not done:
            response = requests.request(
                'GET',f'{url}&page={page}',headers=header)
            headers = dict(response.headers)
            status_code = response.status_code
            response = response.json()
            if status_code != 200:
                return status_code,results,headers
            total_count = response['total_count']
            page+=1
            results.extend(response['items'])
            total_returned+=per_page
            if total_returned >= total_count:
                done = True
    else:
        response = requests.request(
            'GET',f'{url}&page={page}',headers=header)
        headers = dict(response.headers)
        status_code = response.status_code
        response = response.json()
        if status_code != 200:
            return status_code,results,headers
        return status_code,response['items'],headers
    return status_code,results,headers

def search_lazy(endpoint,query,sort=None,order=None,page=1,per_page=100):
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
    """
    header = {'Content-Type': 'application/json'}
    url = f'{GITHUB_API}/search/{endpoint}?q={query}&per_page={per_page}'
    if sort:
        url = f'{url}&sort={sort}'
    if order:
        url = f'{url}&order={order}'
    
    done = False
    total_returned = 0
    while not done:
        response = requests.request(
            'GET',f'{url}&page={page}',headers=header)
        headers = dict(response.headers)
        status_code = response.status_code
        response = response.json()

        if status_code != 200:
            yield status_code,[],headers
            return
        total_count = response['total_count']
        page+=1
        results = response['items']
        yield status_code,results,headers
        total_returned+=per_page
        if total_returned >= total_count:
            done = True
import os
import requests

GITHUB_API = os.getenv('GITHUB_API')


def get_users(query,sort=None,order=None,page=1,per_page=100,strict=False):
    """
    https://developer.github.com/v3/search/#search-users
    https://help.github.com/en/github/searching-for-information-on-github/searching-users

    """
    header = {'Content-Type': 'application/json'}
    url = f'{GITHUB_API}/search/users?q={query}&per_page={per_page}'
    if sort:
        url = f'{url}&sort={sort}'
    if order:
        url = f'{url}&order={order}'
    
    users =[]
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
                return status_code,users,headers
            total_count = response['total_count']
            page+=1
            users.extend(response['items'])
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
            return status_code,users,headers
        return status_code,response['items'],headers
    return status_code,users,headers

def get_users_lazy(query,sort=None,order=None,page=1,per_page=100):
    """
    https://developer.github.com/v3/search/#search-users
    https://help.github.com/en/github/searching-for-information-on-github/searching-users

    """
    header = {'Content-Type': 'application/json'}
    url = f'{GITHUB_API}/search/users?q={query}&per_page={per_page}'
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
        users = response['items']
        yield status_code,users,headers
        total_returned+=per_page
        if total_returned >= total_count:
            done = True
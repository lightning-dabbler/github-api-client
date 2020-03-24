import requests
from constants import GITHUB_API

def emojis():
    """
    `Retrieves all available emojis on GitHub`
    """
    header = {'Content-Type': 'application/json'}
    request_url = f'{GITHUB_API}/emojis'
    response = requests.request(
            'GET',request_url,headers=header)
    headers = dict(response.headers)
    status_code = response.status_code
    if status_code != 200:
        return status_code,{},headers
    response = response.json()
    return status_code,response,headers

    



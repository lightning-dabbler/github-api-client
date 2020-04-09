import requests
import utils
from constants import GITHUB_API

import logging
logger = logging.getLogger(__name__)

def emojis():
    """
    `Retrieves all available emojis on GitHub`

    `returns tuple(status_code:int,response:dict,headers:dict)`
    """
    logger.info('emojis wrapper endpoint')
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

    



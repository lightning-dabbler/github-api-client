import search,emojis,trending
import re
import logging

logger = logging.getLogger(__name__)

def str_url_params_fix(arg):
    return re.sub(r'\s+|\++','+',arg,flags=re.IGNORECASE)

def h_trending(request_body, developers, since):
    """
    - Executes trending.trending and returns a dictionary
    of results 
    
    `return {headers,status_code,items}`
    """
    params = {"developers":developers,"since":since}
    logger.debug(f'Params = {params}')
    if developers:
        request_body['developers'] = developers
    if since:
        request_body['since'] = since
    if request_body:
        status_code,items,headers = trending.trending(**request_body)
    else:
        status_code,items,headers = trending.trending()
    results = {
        'headers':headers,
        'status_code':status_code,
        'items':items
    }
    logger.debug(f'status_code = {status_code} num_items = {len(items)}')
    return results

def h_search(endpoint,query,sort,order,per_page,page):
    """
    - Executes search.search and returns a dictionary
    of results 
    
    `return {headers,status_code,items}`
    """
    current_search_params = {
        'query':query,
        'sort':sort,
        'order':order,
        'per_page':per_page,
        'page':page
    }

    logger.debug(f'current_search_params = {current_search_params}')
    status_code,items,headers = search.search(endpoint,query,sort=sort,
        order=order,page=page,per_page=per_page,strict=True)
    
    results = {
        'headers':headers,
        'status_code':status_code,
        'items':items
    }
    logger.debug(f'status_code = {status_code} num_items = {len(items)}')
    return results

def h_emojis(emoji):
    """
    - Executes emojis.emojis and returns a dictionary
    of results 
    
    `return {headers,status_code,emoji if exists else items}`
    """
    status_code,response,headers = emojis.emojis()

    logger.debug(f"emoji = {emoji}" if emoji else "No Emoji Specified")
    results = {
        'headers':headers,
        'status_code':status_code,
        'items':response
    }
    if emoji and emoji in response:
        results = {
            'headers':headers,
            'status_code':status_code,
            emoji:response[emoji]
        }
    
    logger.debug(f'status_code = {status_code} {f"{emoji} = {response[emoji]}" if emoji in response else f"num_items = {len(response)}"}')    
    return results
from flask import Blueprint,jsonify,request
from . import helpers
import redis
import os
import json

import logging
logger = logging.getLogger(__name__)

r = redis.from_url(os.environ.get('REDIS_URL_NET'))

cache_bp = Blueprint('cache_bp',__name__)

def __cached_trending(**kwargs):
    logger.debug(f'params = {kwargs}')
    developers = kwargs['developers']
    since = kwargs['since']
    key = kwargs['key']
    ttl = kwargs['ttl']

    results = r.get(key)
    if results == None:
        logger.info(f'No Cached Data @ key {key} !')
        results = helpers.h_trending(developers=developers,since=since)
        r.set(key,json.dumps(results),ex=ttl)
        logger.info(f'Value set @ key {key} TTL = {ttl} !')
    else:
        logger.info(f'Cached Data @ key {key} Retrieved !')
        results = json.loads(results)
    return results


@cache_bp.route('/api/cached/trending',methods=['GET'])
def cached_trending():
    logger.info(f'Route = {request.url}')

    developers = bool(request.args.get('developers',False))
    since = request.args.get('since',None)
    refresh = bool(request.args.get('refresh',False))
    ttl = 60*60*5
    freqs = ['daily','weekly','monthly']

    if since not in freqs:
        since = 'daily'
    if developers:
        key_construct = 'trending_dev'
    else:
        key_construct = 'trending_repo'

    params = {
        'key':f'{key_construct}_{since}',
        'developers':developers,
        'since':since,
        'ttl':ttl
    }

    if refresh:
        logger.info(f'Issuing a Refresh for cached Trending; developers = {developers} !')
        
        for freq in freqs:
            results = helpers.h_trending(developers=developers,since=freq)
            r.set(f'{key_construct}_{freq}',json.dumps(results),ex=ttl)
            logger.debug(f'Value set @ key {key_construct}_{freq} TTL = {ttl} !')
    results = __cached_trending(**params)    
    return jsonify(results)

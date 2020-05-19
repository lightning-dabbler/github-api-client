from flask import Blueprint,jsonify,request
from . import helpers
import redis
import os
import json
from rediscluster import RedisCluster
import logging
logger = logging.getLogger(__name__)

APP_ENV = os.environ.get('APP_ENV','development')

if APP_ENV == 'production':
    logger.info('Redis Production Cluster Subnet: 10.0.0.0/16 Ports: 6380-6385')

    startup_nodes = [
        {"host":"10.0.0.11","port":6380},
        {"host":"10.0.0.12","port":6381},
        {"host":"10.0.0.13","port":6382},
        {"host":"10.0.0.14","port":6383},
        {"host":"10.0.0.15","port":6384},
        {"host":"10.0.0.16","port":6385}
    ]
    r = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
else:
    REDIS_URL_NET = os.environ.get('REDIS_URL_NET')
    logger.info(f'Redis Development node {REDIS_URL_NET}')
    r = redis.from_url(REDIS_URL_NET)

cache_bp = Blueprint('cache_bp',__name__)




@cache_bp.route('/cached/trending',methods=['GET'])
def cached_trending():
    logger.info(f'Route = {request.url}')

    developers = request.args.get('developers',False)
    developers = True if helpers.str_lower_rem_l_t_whitespace(developers) == 'true' else False

    since = request.args.get('since','')
    since = helpers.str_lower_rem_l_t_whitespace(since)
    
    refresh = request.args.get('refresh',False)
    refresh = True if helpers.str_lower_rem_l_t_whitespace(refresh) == 'true' else False
    
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
        'ttl':ttl,
        'r':r
    }

    if refresh:
        logger.info(f'Issuing a Refresh for cached Trending; developers = {developers} !')
        
        for freq in freqs:
            results = helpers.h_trending(developers=developers,since=freq)
            r.set(f'{key_construct}_{freq}',json.dumps(results),ex=ttl)
            logger.debug(f'Value set @ key {key_construct}_{freq} TTL = {ttl} !')
    results = helpers.cached_trending_util(**params)    
    return jsonify(results)

@cache_bp.route('/cached/emojis/<path:emoji>',methods=['GET'])
def cached_emojis(emoji):
    logger.info(f'Route = {request.url}')
    emoji = emoji.strip().lower()
    results = r.get(emoji)
    ttl = 60*60*20
    if results == None:
        logger.info(f'No Cached Data @ key {emoji} !')
        results = helpers.h_emojis(emoji)
        if emoji in results:
            results = {
                'name':emoji,
                'exists':True,
                'img':results[emoji]
            }
        else:
            results = {'name':emoji,'exists':False}
        r.set(emoji,json.dumps(results),ex=ttl)
        logger.debug(f'Value set @ key {emoji} TTL = {ttl} !')
    else:
        logger.info(f'Cached Data @ key {emoji} Retrieved !')
        results = json.loads(results)

    return jsonify(results)
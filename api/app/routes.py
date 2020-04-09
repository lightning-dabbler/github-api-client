from flask import current_app as app, jsonify,request
from . import helpers

import logging

logger = logging.getLogger(__name__)



# API ROUTES
@app.route('/',methods=['GET'])
def home():
    logger.info(f'Route = {request.url}')
    logger.info('Root Route Successfully Pinged!')
    resources = {
        'search':"http://localhost:5064/api/search",
        'emojis':"http://localhost:5064/api/emojis",
        'trending':"http://localhost:5064/api/trending"
    }
    response = {
        'status_code':200,
        'resources':resources
    }
    return jsonify(response)

@app.route('/api/search',methods=['GET'])
def search_resource():
    logger.info(f'Route = {request.url}')
    response = {
    "uri":"http://localhost:5064/api/search/<string:endpoint>/<path:query>",
    "endpoint":{
        "values":[
        "repositories",
        "users",
        "commits"
    ],
        "optional":False
    },
    "query": {
        "documentation_url": "https://developer.github.com/v3/search",
        "example":"http://localhost:5064/api/search/commits/test+repo:vuejs/vue",
        "optional":False
    }
    }
    return jsonify(response)


@app.route('/api/search/<string:endpoint>/<path:query>',methods=['GET'])
def query_search(endpoint,query):
    logger.info(f'Route = {request.url}')

    sort = request.args.get('sort',None)
    order = request.args.get('order',None)

    # "+" becomes \s so replace to + so API can read correctly
    if type(sort) == str: sort = helpers.str_url_params_fix(sort)
    if type(order) == str: order = helpers.str_url_params_fix(order)
    
    per_page = int(request.args.get('per_page',100))
    page = int(request.args.get('page',1))

    results = helpers.h_search(endpoint, query, sort, order, per_page, page)
    return jsonify(results)

@app.route('/api/emojis',methods=['GET'])
def query_emojis():
    logger.info(f'Route = {request.url}')
    emoji = request.args.get('emoji',None)
    if emoji: emoji = helpers.str_url_params_fix(emoji)
    
    results = helpers.h_emojis(emoji)

    return jsonify(results)

@app.route('/api/trending',methods=['GET'])
def query_trending():
    logger.info(f'Route = {request.url}')
    developers = bool(request.args.get('developers',False))
    since = request.args.get('since',None)
    if since:
        results = helpers.h_trending(developers=developers, since=since)
    else:
        results = helpers.h_trending(developers=developers)
    return jsonify(results)


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
        'search':"http://localhost:5064/search",
        'emojis':"http://localhost:5064/emojis",
        'trending':"http://localhost:5064/trending"
    }
    response = {
        'status_code':200,
        'resources':resources
    }
    return jsonify(response)

@app.route('/search',methods=['GET'])
def search_resource():
    logger.info(f'Route = {request.url}')
    response = {
    "uri":"http://localhost:5064/search/<string:endpoint>/<path:query>",
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
        "example":"http://localhost:5064/search/commits/test+repo:vuejs/vue",
        "optional":False
    }
    }
    return jsonify(response)


@app.route('/search/<string:endpoint>/<path:query>',methods=['GET'])
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

@app.route('/emojis',methods=['GET'])
def query_emojis():
    logger.info(f'Route = {request.url}')
    emoji = request.args.get('emoji',None)
    if emoji: emoji = helpers.str_url_params_fix(emoji)
    
    results = helpers.h_emojis(emoji)

    return jsonify(results)

@app.route('/trending',methods=['GET'])
def query_trending():
    logger.info(f'Route = {request.url}')
    
    developers = request.args.get('developers',False)
    developers = True if helpers.str_lower_rem_l_t_whitespace(developers) == 'true' else False
    freq = ['daily','weekly','monthly']

    since = request.args.get('since','')
    since = helpers.str_lower_rem_l_t_whitespace(since)
    
    if since in freq:
        results = helpers.h_trending(developers=developers, since=since)
    else:
        results = helpers.h_trending(developers=developers)
    return jsonify(results)


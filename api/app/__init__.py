from flask import Flask,jsonify,request
from flask_cors import CORS
import search,emojis,trending,utils
import re
import logging

logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    CORS(app)
    
    # Private Function
    def __search_helper(search_generators,search_results,**kwargs):
        endpoint = kwargs['endpoint']
        query = kwargs['query']
        sort = kwargs['sort']
        order = kwargs['order']
        page = kwargs['page']
        per_page = kwargs['per_page']
        strict = kwargs['strict']

        if strict == True:
            status_code,items,headers = search.search(endpoint,query,sort=sort,
            order=order,page=page,per_page=per_page,strict=strict)
            search_generators[endpoint] = None
            search_results[endpoint] = {}
            search_results[endpoint]['items']=items
            search_results[endpoint]['headers'] = headers
            search_results[endpoint]['status_code'] = status_code
            logger.debug(f'status_code = {status_code} num_items = {len(items)}')
        else:
            search_generators[endpoint] = search.search_lazy(endpoint,query,sort=sort,
            order=order,page=page,per_page=per_page)
            status_code,items,headers = next(search_generators[endpoint])
            if status_code !=200 or not items:
                search_generators[endpoint] = None
            search_results[endpoint] = {}
            search_results[endpoint]['items']=items
            search_results[endpoint]['headers'] = headers
            search_results[endpoint]['status_code'] = status_code
            logger.debug(f'status_code = {status_code} num_items = {len(items)}')

    def __url_arg_fix(arg):
        return re.sub(r'\s+|\++','+',arg,flags=re.IGNORECASE)

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
        if type(sort) == str: sort = __url_arg_fix(sort)
        if type(order) == str: order = __url_arg_fix(order)
        
        per_page = int(request.args.get('per_page',100))
        page = int(request.args.get('page',1))

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
        return jsonify(results)

    @app.route('/api/emojis',methods=['GET'])
    def query_emojis():
        logger.info(f'Route = {request.url}')
        status_code,response,headers = emojis.emojis()
        emoji = request.args.get('emoji',None)
        if emoji: emoji = __url_arg_fix(emoji)
        logger.debug(f'{f"emoji = {emoji}" if emoji else "No Emoji Specified"}')
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
        return jsonify(results)

    @app.route('/api/trending',methods=['GET'])
    def query_trending():
        logger.info(f'Route = {request.url}')
        request_body = {}
        developers = bool(request.args.get('developers',False))
        since = request.args.get('since',None)
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
        return jsonify(results)
    
    return app
    

if __name__ == '__main__':
    # http://localhost:5064/api/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc
    
    # http://localhost:5064/api/search/users/lightn?

    # http://localhost:5064/api/search/commits/test+repo:vuejs/vue

    # http://localhost:5064/api/emojis?emoji=octocat

    #http://localhost:5064/api/trending?since=weekly
    #http://localhost:5064/api/trending?developers=true&since=monthly
    app = create_app()
    app.run(host='0.0.0.0',port=2064,debug=True)


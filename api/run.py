from flask import Flask,jsonify,request
import search,emojis
import re
import sys

app = Flask(__name__)

# Search Globals
search_generators = {}
search_query_params = {}
search_results = {}

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

def __url_arg_fix(arg):
    return re.sub(r'\s+|\++','+',arg,flags=re.IGNORECASE)

@app.route('/',methods=['GET'])
def home():
    response = {
        'status_code':200,
        'headers':{'Route':'Home'},
        'items':[]
    }
    return jsonify(response)

@app.route('/search/<string:endpoint>/<path:query>',methods=['GET'])
def query_search(endpoint,query):
    global generators,search_query_params,search_results

    sort = request.args.get('sort',None)
    order = request.args.get('order',None)

    # "+" becomes \s so replace to + so API can read correctly
    if type(sort) == str: sort = __url_arg_fix(sort)
    if type(order) == str: order = __url_arg_fix(order)
    
    per_page = int(request.args.get('per_page',100))
    page = int(request.args.get('page',1))
    strict = bool(request.args.get('strict',False))
    refresh = bool(request.args.get('refresh',False))
    current_search_params = {
        'query':query,
        'sort':sort,
        'order':order,
        'per_page':per_page,
        'page':page,
        'strict':strict
    }

    print(f'refresh = {refresh}, current_search_params = {current_search_params}',file= sys.stderr)

    if refresh == True:
        search_query_params[endpoint] = current_search_params
        __search_helper(search_generators,search_results,endpoint=endpoint,**current_search_params)

    elif endpoint in search_query_params:
        cached_params = search_query_params[endpoint]
        if cached_params == current_search_params and search_generators[endpoint]!=None:
            try:
                status_code,items,headers = next(search_generators[endpoint])
                if status_code !=200 or not items:
                    search_generators[endpoint] = None
                search_results[endpoint]['items'].extend(items)
                search_results[endpoint]['headers'] = headers
                search_results[endpoint]['status_code'] = status_code
            except StopIteration:
                search_generators[endpoint] = None
                pass
        elif cached_params == current_search_params:
            pass
        else:
            search_query_params[endpoint] = current_search_params
            __search_helper(search_generators,search_results,endpoint=endpoint,**current_search_params)

    else:
        search_query_params[endpoint] = current_search_params
        __search_helper(search_generators,search_results,endpoint=endpoint,**current_search_params)        

    return jsonify(search_results[endpoint])

@app.route('/emojis',methods=['GET'])
def query_emojis():
    status_code,response,headers = emojis.emojis()
    emoji = request.args.get('emoji',None)
    if emoji: emoji = __url_arg_fix(emoji)

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
    return jsonify(results)
    



if __name__ == '__main__':
    # http://localhost:5064/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc
    # http://localhost:5064/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc&refresh=true
    
    # http://localhost:5064/search/users/lightn?
    # http://localhost:5064/search/users/lightn?refresh=true

    # http://localhost:5064/search/commits/test+repo:vuejs/vue
    # http://localhost:5064/search/commits/test+repo:vuejs/vue?refresh=true
    app.run(host='0.0.0.0',port=2064,debug=True)


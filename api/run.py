from flask import Flask,jsonify,request
import search
import re

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    response = {
        'status_code':200,
        'headers':{'Route':'Home'},
        'items':[]
    }
    return jsonify(response)

@app.route('/search/<string:endpoint>/<string:query>',methods=['GET'])
def query_search(endpoint,query):
    
    sort = request.args.get('sort',None)
    order = request.args.get('order',None)

    # "+" becomes \s so replace to + so API can read correctly
    if type(sort) == str: sort = re.sub(r'\s+|\++','+',sort,flags=re.IGNORECASE)
    if type(order) == str: order = re.sub(r'\s+|\++','+',order,flags=re.IGNORECASE)
    
    per_page = int(request.args.get('per_page',100))
    page = int(request.args.get('page',1))
    strict = bool(request.args.get('strict',False))
    
    status_code,items,headers = search.search(endpoint,query,sort=sort,
    order=order,page=page,per_page=per_page,strict=strict)
    response = {
        'status_code':status_code,
        'headers':headers,
        'items':items
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2064,debug=True)

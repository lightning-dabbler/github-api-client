from flask import Flask
import utils
from flask_cors import CORS
from flask_session import Session

sess = Session()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    CORS(app)
    sess.init_app(app)

    with app.app_context():
        from . import routes
        from . import sessioned_routes

        app.register_blueprint(sessioned_routes.session_bp)
    
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


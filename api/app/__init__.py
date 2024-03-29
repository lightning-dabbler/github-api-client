import utils
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    app.config.from_object("config")
    CORS(app, resources={r"/*": {"origins": "*"}})

    with app.app_context():
        from . import cached_routes, routes

        app.register_blueprint(cached_routes.cache_bp)

    return app


if __name__ == "__main__":
    # http://localhost:5064/api/search/repositories/stars:>1+forks:>1?sort=stars+forks&order=desc

    # http://localhost:5064/api/search/users/lightn?

    # http://localhost:5064/api/search/commits/test+repo:vuejs/vue

    # http://localhost:5064/api/emojis?emoji=octocat

    # http://localhost:5064/api/trending?since=weekly
    # http://localhost:5064/api/trending?developers=true&since=monthly
    app = create_app()
    app.run(host="0.0.0.0", port=2064, debug=True)

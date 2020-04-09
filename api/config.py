import os
import redis

APP_ENV = os.environ.get('APP_ENV','development')
SESSION_TYPE = 'redis'
PERMANENT_SESSION_LIFETIME = 60*60
SESSION_REDIS = redis.from_url(os.environ.get('REDIS_URL_NET'))

if APP_ENV == 'production':
    FLASK_ENV = APP_ENV
    DEBUG = False
else:
    FLASK_ENV = 'development'
    DEBUG = True
    


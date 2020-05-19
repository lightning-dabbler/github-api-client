import os

APP_ENV = os.environ.get('APP_ENV','development')

if APP_ENV == 'production':
    FLASK_ENV = APP_ENV
    DEBUG = False
else:
    FLASK_ENV = 'development'
    DEBUG = True
    


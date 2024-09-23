from flask import Flask
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS
from .database.models import setup_db
from .api import api
from .errors import errors
from .cors import cors

def create_app(test_config=None):

    app = Flask("coffee")

    if test_config is None:
        setup_db(app)
    else:
        setup_db(app, filename=test_config.get('SQL_LITE_FILENAME'))
    
    CORS(app)

    cors(app)
    api(app)
    errors(app)

    return app

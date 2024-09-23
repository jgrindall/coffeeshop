from flask import Flask
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS
from .database.models import setup_db, db_drop_and_create_all
from .api import api
from .errors import errors

def create_app(test_config=None):

    app = Flask("coffee")

    if test_config is None:
        setup_db(app)
    else:
        setup_db(app, filename=test_config.get('SQL_LITE_FILENAME'))
    
    CORS(app)

    db_drop_and_create_all()

    api(app)
    errors(app)

    return app

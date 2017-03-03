
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
# after the db variable initialization
login_manager = LoginManager()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')
db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db)


# def create_app(config_name):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object(app_config[config_name])
#     app.config.from_pyfile('config.py')
#     # db.init_app(app)
#     from app import api
#     return app

#loading API's from ./api/
from app import api

#importing models 
from app import models

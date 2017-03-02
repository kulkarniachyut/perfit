
from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

from app import api

# Load the config file
app.config.from_object('config')

from flask import Flask
from app import app
# from app import create_app

register = Flask(__name__)

@app.route('/register')
def register():
    return "register here"

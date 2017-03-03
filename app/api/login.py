from flask import Flask
from app import app
# from app import create_app

login = Flask(__name__)

@app.route('/login')
def login():
    return "login here"

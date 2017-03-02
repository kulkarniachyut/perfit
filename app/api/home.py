from flask import Flask
from app import app

home = Flask(__name__)

@app.route('/home')
def index():
    return "welcome home"

from flask import Flask
from app import app
# from app import create_app

homepage = Flask(__name__)

@app.route('/')
def homepage():
    return "welcome home"

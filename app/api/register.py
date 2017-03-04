from flask import Flask
from app import app
# from app import create_app

register = Flask(__name__)

@app.route('/register' methods = [GET])
def register():
    return {"statusCode" : 200 , "message" : "registration page"}

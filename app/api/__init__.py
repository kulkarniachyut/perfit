from flask import Flask
from app import app
# from app import create_app
# app = create_app('development')

'''API's '''
from homepage import homepage
from register import register
from login import login
# from profile import profile

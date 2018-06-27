from flask import Flask
from config import app_config
from apiV2.database import Database

db =  Database()

def initialize_app(config_name="development"):
    """initializing app in development mode"""
    app = Flask(__name__, instance_relative_config=True) #creating our WSGI APP Object
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    return app

    
from flask import Flask
from config import app_config
from ..models.database import Database
from ..routes.user import user_route ,auth

db =  Database()

def initialize_app(config_name="development"):
    """initializing app in development mode"""
    app = Flask(__name__, instance_relative_config=True) #creating our WSGI APP Object
    app.config.from_object(app_config[config_name])
    db.__init__()
    app.register_blueprint(user_route,url_prefix="/api/v2/users")
    app.register_blueprint(auth,url_prefix="/api/v2/auth")
    return app

    
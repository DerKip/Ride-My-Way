from flask import Flask
from config import app_config
from ..routes.driver import driver_route 
from ..routes.user import user_route ,user_driver_route


def initialize_app(config_name="development"):
    """initializing app in development mode"""
    app = Flask(__name__, instance_relative_config=True) #creating our WSGI APP Object
    app.config.from_object(app_config[config_name])
    app.register_blueprint(driver_route, url_prefix="/api/v1/driver")
    app.register_blueprint(user_route,url_prefix="/api/v1/user")
    app.register_blueprint(user_driver_route,url_prefix="/api/v1")
    app.config['SECRET_KEY'] = 'thisIsMySecrectKey'
    return app

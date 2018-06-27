import os 
from dotenv import load_dotenv
from pathlib import Path   

env_path = Path('.') / '.env' # explicitly providing path to '.env'
load_dotenv(dotenv_path=env_path)
#Reads the key,value pair from .env and adds them to environment variables
class Config():
    """Base configuration class."""
    DEBUG = False   
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD= os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST= os.getenv("DATABASE_HOST")

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

default_config = app_config['development']
"""Run the Application"""
# from apiV1 import app
from apiV2 import app

app = app.initialize_app()

if __name__ == '__main__':
    app.run()
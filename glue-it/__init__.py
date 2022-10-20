# quick-memo/glue-it/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'Hello World!'
    
    return app

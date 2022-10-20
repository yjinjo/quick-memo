# quick-memo/glue-it/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'Hello World!'

    from flask import jsonify, redirect, url_for
    
    @app.route('/test/path/<path:subpath>')
    def path(subpath):
        return subpath
    
    @app.route('/test/urlfor/<path:subpath>')
    def urlfor(subpath):
        return redirect(url_for('path', subpath=subpath))
    
    return app

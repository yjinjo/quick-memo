# /glue_it/__init__.py

from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'secretkey'
    
    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
        
    '''CSRF INIT'''
    csrf.init_app(app)
    
    '''Routes INIT'''
    from glue_it.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404
    
    return app


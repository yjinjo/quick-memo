# quick-memo/glue-it/__init__.py

from flask import Flask


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        app.logger.info('RUN HELLOWORLD')
        return 'hello world'
    
    ''' Request Hook '''
    from flask import g, current_app
    
    @app.before_first_request
    def before_first_request():
        app.logger.info('BEFORE_FIRST_REQUEST')
    
    @app.before_request
    def before_request():
        g.test=True
        app.logger.info('BEFORE_REQUEST')
        
    @app.after_request
    def after_request(response):
        app.logger.info(f'g.test: {g.test}')
        # app.logger.info(f'current_app.config: {current_app.config}')
        app.logger.info('AFTER_REQUEST')
        
        return response
    
    @app.teardown_request
    def teardown_request(exception):
        app.logger.info('TEARDOWN_REQUEST')
    
    return app

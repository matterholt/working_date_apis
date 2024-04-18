import os
from flask import Flask
from src.features import bp as features_bp



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE= os.path.join(app.instance_path, 'src_event.sqlite'),
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from src.database import db
    db.init_app(app)
    

    # Register blueprints here
    app.register_blueprint(features_bp, url_prefix='/features')


    @app.route('/')
    def main():
        return'<h1>Main page</h1>'


    @app.route('/test/')
    def test_page():
        return'<h1>Testing the Flask</h1>'

    return app
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    from .views import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app

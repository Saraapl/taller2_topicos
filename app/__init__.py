from flask import Flask
import os

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    templates_path = os.path.join(base_dir, "templates")

    app = Flask(__name__, template_folder=templates_path)

    from app.routes import bp
    app.register_blueprint(bp)

    return app

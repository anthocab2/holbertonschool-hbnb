from flask import Flask
from flask_cors import CORS

from config import Config


def create_app(config_class=Config):
    """
    Application factory.
    """

    app = Flask(__name__)

    app.config.from_object(config_class)

    CORS(app)

    return app

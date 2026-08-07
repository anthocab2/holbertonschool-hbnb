from flask import Flask
from flask_cors import CORS

from config import Config


def create_app(config_class=Config):
    """
    Application factory function.

    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_class)

    # Enable CORS
    CORS(app)


    return app

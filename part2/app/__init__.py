"""Application factory module."""

from flask import Flask
from flask_restx import Api

from app.api.v1 import amenities_ns, places_ns, reviews_ns, users_ns


def create_app(config_class="config.DevelopmentConfig"):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Evolution API",
    )

    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(amenities_ns, path="/api/v1/amenities")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(reviews_ns, path="/api/v1/reviews")

    return app

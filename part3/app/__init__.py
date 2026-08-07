from flask import Flask
from flask_cors import CORS

from config import Config

from app.extensions import db, bcrypt, jwt



def create_app(config_class=Config):
    """
    Application factory.
    """

    app = Flask(__name__)


    app.config.from_object(
        config_class
    )


    CORS(app)


    db.init_app(app)

    bcrypt.init_app(app)

    jwt.init_app(app)


    with app.app_context():

        db.create_all()


    from app.api.v1.auth import auth_bp
    from app.api.v1.users import users_bp
    from app.api.v1.places import places_bp
    from app.api.v1.reviews import reviews_bp
    from app.api.v1.amenities import amenities_bp



    app.register_blueprint(
        auth_bp,
        url_prefix="/api/v1/auth"
    )


    app.register_blueprint(
        users_bp,
        url_prefix="/api/v1/users"
    )


    app.register_blueprint(
        places_bp,
        url_prefix="/api/v1/places"
    )


    app.register_blueprint(
        reviews_bp,
        url_prefix="/api/v1/reviews"
    )


    app.register_blueprint(
        amenities_bp,
        url_prefix="/api/v1/amenities"
    )


    return app

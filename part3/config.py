import os


class Config:
    """
    Base configuration.
    """

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "hbnb-secret-key"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///hbnb.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "jwt-secret-key"
    )


class DevelopmentConfig(Config):
    """
    Development configuration.
    """

    DEBUG = True


class TestingConfig(Config):
    """
    Testing configuration.
    """

    TESTING = True

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///:memory:"
    )


class ProductionConfig(Config):
    """
    Production configuration.
    """

    DEBUG = False

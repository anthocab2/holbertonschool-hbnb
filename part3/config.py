import os


class Config:
    """
    Base configuration.
    """

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "default-secret-key"
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


class ProductionConfig(Config):
    """
    Production configuration.
    """

    DEBUG = False

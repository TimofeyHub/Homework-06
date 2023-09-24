from pathlib import Path
from os import getenv

BASE_DIR = Path(__file__)
DEFAULT_DB_URL = "postgresql://username:passwd@pg:5432/blog"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DEFAULT_DB_URL,
)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_ECHO = False
    SECRET_KEY = "ddasdh123jhjkdbasj"


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False

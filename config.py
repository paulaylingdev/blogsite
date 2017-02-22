"""Application configuration file."""
# Flask
DEBUG = False

# Flask SQLAlchemy
SQLALCHEMY_DATABASE_URI = "sqlite:///foo.db"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-HTMLmin
MINIFY_PAGE = True

# Flask Bcrypt
BCRYPT_LOG_ROUNDS = 14

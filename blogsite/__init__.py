"""blogsite package."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_htmlmin import HTMLMIN

# Setting up flask application object
app = Flask(__name__, instance_relative_config=True)

# Configuration settings reading
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Create the database handler using the flask application
db = SQLAlchemy(app)

# Setup htmlmin extension
HTMLMIN(app)

# db object needs to exist before this
from .views import views
# app object needs to exist before this
from .util import assets

# Registering views blueprint
app.register_blueprint(views)

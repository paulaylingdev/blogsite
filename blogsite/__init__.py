"""blogsite package."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import views

# Setting up flask application object
app = Flask(__name__, instance_relative_config=True)

# Configuration settings reading
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Registering views blueprint
app.register_blueprint(views)

# Create the database handler using the flask application
db = SQLAlchemy(app)

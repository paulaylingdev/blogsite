"""Factory for creating the flask application."""
from flask import Flask
from flask_htmlmin import HTMLMIN


def create_app(name, settings_override=None, templates_folder=None):
    """Factory method for creating a application."""
    # Setting up flask application object
    if templates_folder is None:
        app = Flask(name, instance_relative_config=True)
    else:
        app = Flask(name, instance_relative_config=True, template_folder=templates_folder)

    # Configuration settings reading
    app.config.from_object('config')
    # Try to read instance config, print warning if it doesn't exist.
    if not app.config.from_pyfile('config.py', silent=True):
        print("Warning! Default Configuration in use, please define a configuration file under a instance folder")

    if settings_override:
        app.config.update(settings_override)

    # Init the database handler using the flask application
    from .database import db, app_bcrypt
    db.init_app(app)
    app_bcrypt.init_app(app)

    # Init the flask assets extension object
    from .util.assets import assets
    assets.init_app(app)

    # Init the flask html min extension object
    htmlmin = HTMLMIN()
    htmlmin.init_app(app)

    # Registering views blueprint
    from .views import views
    app.register_blueprint(views)

    return app

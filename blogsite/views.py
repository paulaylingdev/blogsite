"""The views of the blogsite application."""
from flask import Blueprint, render_template

# Creating the views blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    """The index page route."""
    return render_template('index.html')

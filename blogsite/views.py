"""The views of the blogsite application."""
from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def index():
    """The index page route."""
    return "A simple index page"

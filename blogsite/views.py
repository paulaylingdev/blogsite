"""The views of the blogsite application."""
from flask import Blueprint, render_template
from .models import Post

# Creating the views blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    """The index page route."""
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

"""The views of the blogsite application."""
from flask import Blueprint, render_template
from sqlalchemy import desc
from .models import Post

# Creating the views blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    """The index page route."""
    posts = Post.query.order_by(desc(Post.pub_date)).all()
    return render_template('index.html', posts=posts)

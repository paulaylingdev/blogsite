"""The views of the blogsite application."""
from flask import Blueprint, render_template
from sqlalchemy import desc
from .models import Post, Tag

# Creating the views blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    """The index page route."""
    posts = Post.query.order_by(desc(Post.pub_date)).all()
    return render_template('index.html', posts=posts)


@views.route('/post/<int:post_id>')
def single_post(post_id):
    """Create a view with a single blog post on it."""
    post = Post.query.get_or_404(post_id)
    return render_template('index.html', posts=[post])


@views.route('/tag/<int:tag_id>')
def posts_with_tag(tag_id):
    """Create a view with all posts related to a tag."""
    tag = Tag.query.get_or_404(tag_id)
    return render_template('index.html', posts=tag.posts)

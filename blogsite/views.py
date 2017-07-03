"""The views of the blogsite application."""
from flask import Blueprint, render_template, redirect, url_for, flash
from sqlalchemy import desc

from .forms import UsernamePasswordForm
from .models import Post, Tag

# Creating the views blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    """The index page route."""
    posts = Post.query.order_by(desc(Post.pub_date)).all()
    return render_template('posts.html', posts=posts)


@views.route('/login', methods=["GET", "POST"])
def login():
    """Present login form to user."""
    form = UsernamePasswordForm()
    if form.validate_on_submit():
        # TODO - Login User if valid account
        return redirect(url_for('views.index'))
    else:
        flash_errors(form)
    return render_template('login.html', form=form)


@views.route('/post/<int:post_id>')
def single_post(post_id):
    """Create a view with a single blog post on it."""
    post = Post.query.get_or_404(post_id)
    return render_template('posts.html', posts=[post])


@views.route('/tag/<int:tag_id>')
def posts_with_tag(tag_id):
    """Create a view with all posts related to a tag."""
    tag = Tag.query.get_or_404(tag_id)
    summarytext = 'Blog posts containing tag : ' + tag.name
    return render_template('post_summarys.html', posts=tag.posts,
                           summarytext=summarytext)


@views.errorhandler(404)
def page_not_found(e):
    """Custom view for HTTP Error 404."""
    return render_template('404.html'), 404


def flash_errors(form):
    """Take a form and flash its errors."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

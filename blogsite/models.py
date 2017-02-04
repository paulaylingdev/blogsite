"""Collection of Models used in blogsite."""
from . import db


class Post(db.Model):
    """Model representing a blog post."""

    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    body = db.Column(db.String(4096))

"""Collection of Models used in blogsite."""
from . import db


class Post(db.Model):
    """Model representing a blog post."""

    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    body = db.Column(db.String(4096))

    def __init__(self, title, body):
        """Constructor for Post."""
        self.title = title
        self.body = body

    def __repr__(self):
        """Representation."""
        return '<Post %r:%r>' % self.id, self.title

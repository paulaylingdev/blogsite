"""Initialise database."""
from blogsite import app
from blogsite.database import db

app.app_context().push()
db.create_all()
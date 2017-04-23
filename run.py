"""Main run file for dev."""
from blogsite import app
from werkzeug.contrib.fixers import ProxyFix
import os

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host=os.getenv('IP','0.0.0.0'),port=os.getenv('PORT', '8080'))

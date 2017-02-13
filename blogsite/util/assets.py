"""Flask Assests bundles for packages."""

from flask_assets import Bundle, Environment
from .. import app

bundles = {
    'blogsite_css': Bundle(
        'css/style.css',
        output="gen/index.css"
    )
}

assets = Environment(app)

assets.register(bundles)

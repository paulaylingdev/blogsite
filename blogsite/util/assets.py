"""Flask Assests bundles for packages."""

from flask_assets import Bundle, Environment

bundles = {
    'blogsite_css': Bundle(
        'css/style.css',
        output="gen/style.css",
        filters='cssmin'
    )
}

assets = Environment()

assets.register(bundles)

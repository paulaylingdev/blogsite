"""conftest for pytest."""
import os
import tempfile
import pytest

from blogsite.factory import create_app
from blogsite.database import db as _db
from blogsite.util.assets import assets


TESTDB = 'test_project.db'
TESTDB_PATH = tempfile.mkdtemp() + "{}".format(TESTDB)
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    }
    app = create_app(__name__, settings_override, "../blogsite/templates")

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    # Allows assets to be found under blogsite/static.
    assets.load_path = [os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "blogsite", "static")]

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="session")
def test_app(app):
    """Create a test app client."""
    return app.test_client()


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Create a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session

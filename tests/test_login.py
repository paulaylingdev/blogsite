"""Unit Testing for the Login View."""
import pytest


@pytest.mark.usefixtures("session", "test_app")
class TestLogin:
    """Test Login View Class."""
    def test_login(self, test_app):
        """Test that the login page title is returned and not an error."""
        rv = test_app.get("/login")
        assert b'blogsite - login' in rv.data

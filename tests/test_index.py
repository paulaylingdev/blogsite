"""Unit Testing for Index view."""
import pytest


@pytest.mark.usefixtures("session", "test_app")
class TestIndex:
    """Test the index page call."""

    def test_index(self, test_app):
        """Test that the index returns a html doc."""
        rv = test_app.get('/')
        assert b'<!DOCTYPE html>' in rv.data

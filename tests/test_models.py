"""Unit Testing for blogsite using pytest."""
import pytest
from blogsite.models import Post, Tag


@pytest.mark.usefixtures("session")
class TestPostModel:
    """Test the Post Model."""

    @pytest.fixture
    def tags(self, session):
        """Tag list to be used in Post tests."""
        newtags = [
            Tag("C++"),
            Tag("Python"),
        ]
        session.add(newtags[0])
        session.add(newtags[1])
        session.commit()
        return newtags

    def test_post_object(self, session):
        """Test that a post object can be stored into the database."""
        post = Post("Title", "Body")
        session.add(post)
        session.commit()
        assert post.id > 0

    def test_post_with_tags(self, session, tags):
        """Test creating a post object with multiple tags."""
        post = Post("Title", "Body", tags)
        session.add(post)
        session.commit()
        assert len(Post.query.get(1).tags) == 2

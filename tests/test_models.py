"""Unit Testing for blogsite using pytest."""
import pytest
from blogsite.models import Post, Tag, User
from blogsite.database import app_bcrypt


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


@pytest.mark.usefixtures("session")
class TestUserModel:
    """Test the User Model."""

    @pytest.fixture
    def user(self, session):
        """Create a user and adds it to the database."""
        user = User("username", "password", "email@email.co.uk")
        session.add(user)
        session.commit()

    def test_user_object_creation(self, session, user):
        """Test that a user object can be created."""
        user = User.query.get(1)
        assert user.id > 0

    def test_user_password_getter(self, session, user):
        """Test that the user password getter returns a hash."""
        user = User.query.get(1)
        assert user.password != "password"

    def test_user_password_checker(self, session, user):
        """Test that we can check a users password."""
        user = User.query.get(1)
        assert app_bcrypt.check_password_hash(user.password, "password")

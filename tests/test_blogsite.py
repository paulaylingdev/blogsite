"""Unit Testing for blogsite using pytest."""
from blogsite.models import Post


def test_post_model(session):
    post = Post("Title", "Body")
    session.add(post)
    session.commit()

    assert post.id > 0

import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def test_user(db):
    """
    Pytest fixture that creates a test user in the database.

    This fixture uses the Django's built-in User model's `create_user` method
    to create a test user with username 'testuser' and password '12345'.
    The created user is then returned.

    :param db: pytest fixture that provides database access.
    :return: User object representing the created test user.
    """
    return User.objects.create_user(username='testuser', password='12345')


@pytest.fixture
def test_profile(db, test_user):
    """
    Pytest fixture that creates a test profile in the database.

    This fixture uses the Profile model's `create` method to create a
    test profile associated with the `test_user` created by the `test_user` fixture.
    The created profile is then returned.

    :param db: pytest fixture that provides database access.
    :param test_user: pytest fixture that provides a test user.
    :return: Profile object representing the created test profile.
    """
    return Profile.objects.create(user=test_user, favorite_city='Test City')

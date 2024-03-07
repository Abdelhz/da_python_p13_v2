import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


def test_create_profile(test_profile):
    """
    Test if the test_profile fixture is an instance of Profile model.

    This test checks if the `test_profile` fixture, which should represent a Profile object,
    is indeed an instance of the Profile model.

    :param test_profile: pytest fixture that provides a test profile.
    """
    assert isinstance(test_profile, Profile)


def test_read_profile(test_profile):
    """
    Test if a profile can be retrieved from the database by their user's username.

    This test attempts to retrieve the `test_profile` from the database by their user's username.
    If the profile exists in the database, this should return a Profile object.

    :param test_profile: pytest fixture that provides a test profile.
    """
    assert Profile.objects.get(user__username=test_profile.user.username)


def test_update_profile(test_profile):
    """
    Test if updating a profile's favorite_city is reflected in the database.

    This test first updates the favorite_city of the `test_profile` in the database, and then
    attempts to retrieve a profile with the new favorite_city from the database. If the update
    was successful, this should return a Profile object.

    :param test_profile: pytest fixture that provides a test profile.
    """
    Profile.objects.filter(user__username=test_profile.user.username).update(favorite_city='New City')
    assert Profile.objects.get(user__username=test_profile.user.username).favorite_city == 'New City'


def test_delete_profile(test_profile):
    """
    Test if deleting a profile removes it from the database.

    This test first deletes the `test_profile` from the database, and then attempts to retrieve
    the same profile from the database. Since the profile has been deleted, this should raise a
    `Profile.DoesNotExist` exception.

    :param test_profile: pytest fixture that provides a test profile.
    """
    Profile.objects.get(user__username=test_profile.user.username).delete()
    with pytest.raises(Profile.DoesNotExist):
        Profile.objects.get(user__username=test_profile.user.username)


def test_profile_str(test_profile):
    """
    Test the string representation of the Profile model.

    This test checks if the `__str__` method of the `Profile` model returns the username of the
    linked User instance.

    :param test_profile: pytest fixture that provides a test profile.
    """
    assert str(test_profile) == test_profile.user.username


def test_delete_user(test_user):
    """
    Test if deleting a user removes them from the database.

    This test first deletes the `test_user` from the database, and then attempts to retrieve
    the same user from the database. Since the user has been deleted, this should raise a
    `User.DoesNotExist` exception.

    :param test_user: pytest fixture that provides a test user.
    """
    User.objects.get(username=test_user.username).delete()
    with pytest.raises(User.DoesNotExist):
        User.objects.get(username=test_user.username)


def test_update_user(test_user):
    """
    Test if updating a user's username is reflected in the database.

    This test first updates the username of the `test_user` in the database, and then attempts
    to retrieve a user with the new username from the database. If the update was successful,
    this should return a User object.

    :param test_user: pytest fixture that provides a test user.
    """
    User.objects.filter(username=test_user.username).update(username='newusername')
    assert User.objects.get(username='newusername')


def test_read_user(test_user):
    """
    Test if a user can be retrieved from the database by their username.

    This test attempts to retrieve the `test_user` from the database by their username. If the
    user exists in the database, this should return a User object.

    :param test_user: pytest fixture that provides a test user.
    """
    assert User.objects.get(username=test_user.username)

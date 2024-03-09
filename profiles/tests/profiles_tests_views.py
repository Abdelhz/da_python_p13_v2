import pytest
from django.urls import reverse
from profiles.models import Profile


def test_index_view(client, test_profile):
    """
    Test if the 'index' view returns a 200 status code and the correct number of profiles.

    This test uses the `client` to send a GET request to the URL for the 'index' view, and checks
    if the response has a status code of 200. It also checks if the number of Profile objects in
    the database is 1, which should be the case if the `test_profile` fixture has been used to
    create a single profile.

    :param client: Django test client.
    :param test_profile: pytest fixture that provides a test profile.
    """
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assert Profile.objects.count() == 1


def test_profile_view(client, test_profile):
    """
    Test if the 'profile' view returns a 200 status code for an existing profile.

    This test uses the `client` to send a GET request to the URL for the 'profile' view, passing
    the username of the `test_profile` as an argument. It checks if the response has a status code
    of 200, which should be the case if the profile exists.

    :param client: Django test client.
    :param test_profile: pytest fixture that provides a test profile.
    """
    url = reverse('profiles:profile', args=[test_profile.user.username])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_with_nonexistent_profile(client):
    """
    Test if the 'profile' view returns a 404 status code for a nonexistent profile.

    This test uses the `client` to send a GET request to the URL for the 'profile' view, passing
    'nonexistent' as the username. Since there is no profile with this username, the view should
    return a 404 status code.

    :param client: Django test client.
    """
    url = reverse('profiles:profile', args=['nonexistent'])
    response = client.get(url)
    assert response.status_code == 404

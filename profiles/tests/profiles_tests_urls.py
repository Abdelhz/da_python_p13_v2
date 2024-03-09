from django.urls import reverse, resolve
from profiles import views


def test_index_url():
    """
    Test if the reverse function correctly generates the URL for the 'index' view.

    This test uses the `reverse` function to generate the URL for the 'index' view, and then
    uses the `resolve` function to determine the view function that should handle this URL.
    It checks if the resolved view function is `views.index`.
    """
    url = reverse('profiles:index')
    assert resolve(url).func == views.index


def test_profile_url(test_profile):
    """
    Test if the reverse function correctly generates the URL for the 'profile' view.

    This test uses the `reverse` function to generate the URL for the 'profile' view, passing
    the username of the `test_profile` as an argument. It then uses the `resolve` function to
    determine the view function that should handle this URL. It checks if the resolved view
    function is `views.profile`.

    :param test_profile: pytest fixture that provides a test profile.
    """
    url = reverse('profiles:profile', args=[test_profile.user.username])
    assert resolve(url).func == views.profile

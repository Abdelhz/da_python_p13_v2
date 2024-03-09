from django.urls import reverse, resolve
from lettings import views


def test_index_url():
    """
    Test function to verify the 'lettings:index' URL.

    This function uses the reverse() function to generate the URL for the
    'lettings:index' view and then asserts that the function associated with
    this URL is the 'index' view function in the 'lettings' app.

    """
    url = reverse('lettings:index')
    assert resolve(url).func == views.index


def test_letting_url(test_letting):
    """
    Test function to verify the 'lettings:letting' URL.

    This function uses the reverse() function to generate the URL for
    the 'lettings:letting' view with the ID of the 'test_letting' fixture as an argument.
    It then asserts that the function associated with this URL is the 'letting'
    view function in the 'lettings' app.

    :param test_letting: Pytest fixture that provides a test Letting object.
    """
    url = reverse('lettings:letting', args=[test_letting.id])
    assert resolve(url).func == views.letting

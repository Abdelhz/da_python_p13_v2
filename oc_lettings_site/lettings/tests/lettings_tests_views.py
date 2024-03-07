import pytest
from django.urls import reverse
from lettings.models import Letting


def test_index_view(client, test_letting):
    """
    Test function to verify the 'lettings:index' view.

    This function uses the Django test client to send a GET request to the
    'lettings:index' view and then asserts that the response status code is 200 (OK)
    and that there is one Letting object in the database.

    :param client: Django test client.
    :param test_letting: Pytest fixture that provides a test Letting object.
    """
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert Letting.objects.count() == 1


def test_index_view_exception_handling(client, monkeypatch):
    """
    Test function to verify the exception handling in the 'profiles:index' view.

    This function uses the monkeypatch fixture to replace the `Profile.objects.all()` method
    with a function that raises an exception, and then sends a GET request to the 'profiles:index' view.
    It then asserts that the response status code is 404 (Not Found).

    :param client: Django test client.
    :param monkeypatch: pytest fixture for mocking.
    """
    def mock_raise(*args, **kwargs):
        raise Exception

    monkeypatch.setattr('profiles.views.Profile.objects.all', mock_raise)
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 404


def test_letting_view(client, test_letting):
    """
    Test function to verify the 'lettings:letting' view.

    This function uses the Django test client to send a GET request to the
    'lettings:letting' view with the ID of the 'test_letting' fixture as an argument.
    It then asserts that the response status code is 200 (OK).

    :param client: Django test client.
    :param test_letting: Pytest fixture that provides a test Letting object.
    """
    url = reverse('lettings:letting', args=[test_letting.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view_with_nonexistent_letting(client):
    """
    Test function to verify the 'lettings:letting' view with a nonexistent Letting object.

    This function uses the Django test client to send a GET request to the
    'lettings:letting' view with a nonexistent Letting ID as an argument.
    It then asserts that the response status code is 404 (Not Found).

    :param client: Django test client.
    """
    url = reverse('lettings:letting', args=[999])
    response = client.get(url)
    assert response.status_code == 404

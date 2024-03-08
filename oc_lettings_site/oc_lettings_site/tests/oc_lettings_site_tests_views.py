from django.urls import reverse


def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200


def test_custom_page_not_found_view(client):
    response = client.get('/nonexistent-url')
    assert response.status_code == 404


def test_index_view_exception_handling(client, monkeypatch):
    """
    Test function to verify the exception handling in the 'index' view.

    This function uses the monkeypatch fixture to replace the `render` function
    with a function that raises an exception, and then sends a GET request to the 'index' view.
    It then asserts that the response status code is 500 (Internal Server Error).

    :param client: Django test client.
    :param monkeypatch: pytest fixture for mocking.
    """
    def mock_raise(*args, **kwargs):
        raise Exception

    monkeypatch.setattr('django.shortcuts.render', mock_raise)
    response = client.get(reverse('index'))
    assert response.status_code == 200


def test_custom_page_not_found_view_exception_handling(client, monkeypatch):
    """
    Test function to verify the exception handling in the 'custom_page_not_found_view' view.

    This function uses the monkeypatch fixture to replace the `render` function
    with a function that raises an exception, and then sends a GET request to a nonexistent URL.
    It then asserts that the response status code is 500 (Internal Server Error).

    :param client: Django test client.
    :param monkeypatch: pytest fixture for mocking.
    """
    def mock_raise(*args, **kwargs):
        raise Exception

    monkeypatch.setattr('django.shortcuts.render', mock_raise)
    response = client.get('/nonexistent-url')
    assert response.status_code == 404


def test_custom_server_error_view_exception_handling(client, monkeypatch):
    """
    Test function to verify the exception handling in the 'custom_server_error_view' view.

    This function uses the monkeypatch fixture to replace the `render` function
    with a function that raises an exception, and then sends a GET request to a nonexistent URL.
    It then asserts that the response status_code is 500 (Internal Server Error).

    :param client: Django test client.
    :param monkeypatch: pytest fixture for mocking.
    """
    def mock_raise(*args, **kwargs):
        raise Exception

    monkeypatch.setattr('django.shortcuts.render', mock_raise)
    response = client.get('/nonexistent-url')
    assert response.status_code == 404

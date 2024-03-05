import pytest
from lettings.models import Address, Letting


@pytest.fixture
def test_address(db):
    """
    Pytest fixture that creates and returns a test Address object.

    This fixture uses the Django test database (indicated by the 'db' parameter)
    to create an Address object with predefined test data.
    The Address object is then returned and can be used in tests.

    :param db: Pytest fixture that provides database access.
    :return: A test Address object.
    """
    return Address.objects.create(
        number=123,
        street='Test Street',
        city='Test City',
        state='TS',
        zip_code=12345,
        country_iso_code='TST'
    )


@pytest.fixture
def test_letting(db, test_address):
    """
    Pytest fixture that creates and returns a test Letting object.

    This fixture uses the Django test database (indicated by the 'db' parameter)
    and the 'test_address' fixture to create a Letting object with predefined test data.
    The Letting object is then returned and can be used in tests.

    :param db: Pytest fixture that provides database access.
    :param test_address: Pytest fixture that provides a test Address object.
    :return: A test Letting object.
    """
    return Letting.objects.create(title='Test Letting', address=test_address)

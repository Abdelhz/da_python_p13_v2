import pytest
from lettings.models import Address, Letting


@pytest.fixture
def test_address(db):
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
    return Letting.objects.create(title='Test Letting', address=test_address)

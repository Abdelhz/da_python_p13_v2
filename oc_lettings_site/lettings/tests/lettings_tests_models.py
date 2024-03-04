import pytest
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting

def test_create_letting(test_letting):
    assert isinstance(test_letting, Letting)

def test_create_address_with_long_street_name(db):
    long_street_name = 'a' * 65
    with pytest.raises(ValidationError):
        Address.objects.create(
            number=123,
            street=long_street_name,
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
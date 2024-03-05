import pytest
from lettings.models import Address, Letting


# Create
def test_create_address(test_address):
    assert isinstance(test_address, Address)


def test_create_letting(test_letting):
    assert isinstance(test_letting, Letting)


# Read
def test_read_address(test_address):
    assert Address.objects.get(id=test_address.id)


def test_read_letting(test_letting):
    assert Letting.objects.get(id=test_letting.id)


# Update
def test_update_address(test_address):
    test_address.street = 'Updated Street'
    test_address.save()
    assert Address.objects.get(id=test_address.id).street == 'Updated Street'


def test_update_letting(test_letting):
    test_letting.title = 'Updated Letting'
    test_letting.save()
    assert Letting.objects.get(id=test_letting.id).title == 'Updated Letting'


# Delete
def test_delete_address(test_address):
    test_address_id = test_address.id
    test_address.delete()
    with pytest.raises(Address.DoesNotExist):
        Address.objects.get(id=test_address_id)


def test_delete_letting(test_letting):
    test_letting_id = test_letting.id
    test_letting.delete()
    with pytest.raises(Letting.DoesNotExist):
        Letting.objects.get(id=test_letting_id)

import pytest
from lettings.models import Address, Letting


# Create
def test_create_address(test_address):
    """
    Test function to verify the creation of an Address object.

    This function asserts that the 'test_address' fixture is an instance of the Address model.

    :param test_address: Pytest fixture that provides a test Address object.
    """
    assert isinstance(test_address, Address)


def test_create_letting(test_letting):
    """
    Test function to verify the creation of a Letting object.

    This function asserts that the 'test_letting' fixture is an instance of the Letting model.

    :param test_letting: Pytest fixture that provides a test Letting object.
    """
    assert isinstance(test_letting, Letting)


# Read
def test_read_address(test_address):
    """
    Test function to verify the retrieval of an Address object.

    This function asserts that an Address object with the ID of the 'test_address'
    fixture can be retrieved from the database.

    :param test_address: Pytest fixture that provides a test Address object.
    """
    assert Address.objects.get(id=test_address.id)


def test_read_letting(test_letting):
    """
    Test function to verify the retrieval of a Letting object.

    This function asserts that a Letting object with the ID of the 'test_letting'
    fixture can be retrieved from the database.

    :param test_letting: Pytest fixture that provides a test Letting object.
    """
    assert Letting.objects.get(id=test_letting.id)


# Update
def test_update_address(test_address):
    """
    Test function to verify the update of an Address object.

    This function updates the 'street' field of the 'test_address' fixture,
    saves the changes to the database, and then asserts that the updated
    'street' field of the Address object in the database matches the new value.

    :param test_address: Pytest fixture that provides a test Address object.
    """
    test_address.street = 'Updated Street'
    test_address.save()
    assert Address.objects.get(id=test_address.id).street == 'Updated Street'


def test_update_letting(test_letting):
    """
    Test function to verify the update of a Letting object.

    This function updates the 'title' field of the 'test_letting' fixture,
    saves the changes to the database, and then asserts that
    the updated 'title' field of the Letting object
    in the database matches the new value.

    :param test_letting: Pytest fixture that provides a test Letting object.
    """
    test_letting.title = 'Updated Letting'
    test_letting.save()
    assert Letting.objects.get(id=test_letting.id).title == 'Updated Letting'


# Delete
def test_delete_address(test_address):
    """
    Test function to verify the deletion of an Address object.

    This function deletes the 'test_address' fixture from the database and
    then asserts that an Address.DoesNotExist exception is raised when trying
    to retrieve the deleted Address object from the database.

    :param test_address: Pytest fixture that provides a test Address object.
    """
    test_address_id = test_address.id
    test_address.delete()
    with pytest.raises(Address.DoesNotExist):
        Address.objects.get(id=test_address_id)


def test_delete_letting(test_letting):
    """
    Test function to verify the deletion of a Letting object.

    This function deletes the 'test_letting' fixture from the database and
    then asserts that a Letting.DoesNotExist exception is raised when trying
    to retrieve the deleted Letting object from the database.

    :param test_letting: Pytest fixture that provides a test Letting object.
    """
    test_letting_id = test_letting.id
    test_letting.delete()
    with pytest.raises(Letting.DoesNotExist):
        Letting.objects.get(id=test_letting_id)

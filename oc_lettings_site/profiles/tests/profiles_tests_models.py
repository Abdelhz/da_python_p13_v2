import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from profiles.models import Profile

def test_create_profile(test_profile):
    assert isinstance(test_profile, Profile)


def test_delete_user(test_user):
    User.objects.get(username=test_user.username).delete()
    with pytest.raises(User.DoesNotExist):
        User.objects.get(username=test_user.username)


def test_update_user(test_user):
    User.objects.filter(username=test_user.username).update(username='newusername')
    assert User.objects.get(username='newusername')


def test_read_user(test_user):
    assert User.objects.get(username=test_user.username)
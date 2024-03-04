import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.fixture
def test_user(db):
    return User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def test_profile(db, test_user):
    return Profile.objects.create(user=test_user, favorite_city='Test City')
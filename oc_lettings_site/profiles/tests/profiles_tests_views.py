import pytest
from django.shortcuts import get_object_or_404
from django.urls import reverse
from profiles.models import Profile

def test_index_view(client, test_profile):
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assert Profile.objects.count() == 1

def test_profile_view(client, test_profile):
    url = reverse('profiles:profile', args=[test_profile.user.username])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_profile_view_with_nonexistent_profile(client):
    url = reverse('profiles:profile', args=['nonexistent'])
    response = client.get(url)
    assert response.status_code == 404
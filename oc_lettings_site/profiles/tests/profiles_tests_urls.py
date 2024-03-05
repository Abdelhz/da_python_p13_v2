from django.urls import reverse, resolve
from profiles import views


def test_index_url():
    url = reverse('profiles:index')
    assert resolve(url).func == views.index


def test_profile_url(test_profile):
    url = reverse('profiles:profile', args=[test_profile.user.username])
    assert resolve(url).func == views.profile

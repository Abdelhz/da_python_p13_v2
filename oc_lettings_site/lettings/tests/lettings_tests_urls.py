from django.urls import reverse, resolve
from lettings import views


def test_index_url():
    url = reverse('lettings:index')
    assert resolve(url).func == views.index


def test_letting_url(test_letting):
    url = reverse('lettings:letting', args=[test_letting.id])
    assert resolve(url).func == views.letting

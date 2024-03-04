import pytest
from django.urls import reverse
from lettings.models import Letting

def test_index_view(client, test_letting):
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert Letting.objects.count() == 1

def test_letting_view(client, test_letting):
    url = reverse('lettings:letting', args=[test_letting.id])
    response = client.get(url)
    assert response.status_code == 200

def test_letting_view_with_nonexistent_letting(client):
    url = reverse('lettings:letting', args=[999])
    response = client.get(url)
    assert response.status_code == 404
import pytest
from django.urls import reverse


def test_about_view(client):
    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200
    assert 'OTUS Basic' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_product_list_view(client, product1, product2, category):
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200

    assert 'Test product 1' in response.content.decode('utf-8')
    assert 'Test product 2' in response.content.decode('utf-8')
    assert category.name.encode() in response.content


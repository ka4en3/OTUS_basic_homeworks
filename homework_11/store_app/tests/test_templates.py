import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


@pytest.mark.django_db
def test_product_list_view(client, category, product1, product2):
    """tests of template product_list.html"""
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')

    # Test page title
    assert soup.select_one('h1').text == 'List of goods'

    # Test filter form exists
    filter_form = soup.select_one('form[method="GET"]')
    assert filter_form is not None
    # Test price filter exists
    price_input = filter_form.select_one('input#price')
    assert price_input is not None
    assert price_input.get('type') == 'number'
    # Test submit button exists
    submit_button = filter_form.select_one('button[type="submit"]')
    assert submit_button is not None
    assert submit_button.text.strip() == 'Apply'

    # Test product listing
    product_items = soup.select('ul.list-group li.list-group-item')
    assert len(product_items) == 2  # Assuming product1 and product2 are created in fixtures
    # Check product details are displayed correctly
    for i, product in enumerate([product1, product2]):
        item = product_items[i]
        assert product.name in item.text
        assert str(product.price) in item.text
        assert product.category.name in item.text


@pytest.mark.django_db
def test_product_list_empty(client, category):
    """tests of template product_list.html for emptiness"""
    # Test when no products are available
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')

    # Check empty state message
    empty_message = soup.select_one('ul.list-group')
    assert "Oops! We can't find any goods." in empty_message.text

    # Check that no product items are shown
    product_items = soup.select('ul.list-group li.list-group-item')
    assert len(product_items) == 0


@pytest.mark.django_db
def test_product_filter_by_price(client, category, product1, product2):
    """tests of price filtering of template product_list.html"""
    # Set different prices
    product1.price = 10.00
    product1.save()
    product2.price = 20.00
    product2.save()

    # Test filtering by price
    url = reverse('product_list') + '?price=15.00'
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')

    # Check that only product1 is shown
    product_items = soup.select('ul.list-group li.list-group-item')
    assert len(product_items) == 1
    assert product1.name in product_items[0].text
    assert product2.name not in soup.text

    # Check that the price filter shows the correct value
    price_input = soup.select_one('input#price')
    assert price_input.get('value') == '15.00'
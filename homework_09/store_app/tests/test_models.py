import pytest
from decimal import Decimal
from store_app.models import Product, Category

# Для работы с реальной БД pytest --reuse-db
@pytest.mark.django_db
def test_category_creation(category):
    assert Category.objects.count() == 1
    assert category.name == 'Test category'
    assert str(category) == 'Test category'


@pytest.mark.django_db
def test_product_creation(product1, product2):
    assert Product.objects.count() == 2

    product_1 = Product.objects.get(pk=product1.id)
    assert product1 == product_1
    assert product_1.name == 'Test product 1'
    assert product_1.price == Decimal('100')
    assert product_1.rating == 10
    assert product_1.description == 'test product 1 description'
    assert product_1.category.name == 'Test category'

    product_2 = Product.objects.get(pk=product2.id)
    assert product2 == product_2
    assert product_2.name == 'Test product 2'
    assert product_2.price == Decimal('10.10')
    assert product_2.rating == 1
    assert product_2.description == 'test product 2 description'
    assert product_2.category.name == 'Test category'

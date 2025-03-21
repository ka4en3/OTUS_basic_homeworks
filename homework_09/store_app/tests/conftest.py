import pytest
from decimal import Decimal
from store_app.models import Product, Category


@pytest.fixture
def category():
    return Category.objects.create(name='Test category',
                                   description="test category description")


@pytest.fixture
def product1(category):
    return Product.objects.create(name='Test product 1',
                               description="test product 1 description",
                               price=Decimal('100'),
                               rating=10,
                               category=category
                               )

@pytest.fixture
def product2(category):
    return Product.objects.create(name='Test product 2',
                               description="test product 2 description",
                               price=Decimal('10.10'),
                               rating=1,
                               category=category
                               )
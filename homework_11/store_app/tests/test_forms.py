import pytest
from store_app.models import Product
from store_app.forms import ProductModelForm, ProductDeleteForm


@pytest.mark.django_db
def test_productmodelform_validation(category):
    """tests for form ProductModelForm"""
    form_data = {
        "name": "Model of product",
        "description": "some description of model of product",
        "price": 0,
        "category": category.id,
        "rating": 1,
    }
    form = ProductModelForm(data=form_data)
    assert not form.is_valid()

    form_data_1 = {
        "name": "Model of product 1",
        "description": "some description of model of product 1",
        "price": 123,
        "category": category.id,
        "rating": 1,
    }
    form = ProductModelForm(data=form_data_1)
    assert form.is_valid()
    product_1 = form.save()

    form_data_2 = {
        "name": "Model of product 2",
        "description": "some description of model of product 2",
        "price": 321,
        "category": category.id,
        "rating": 2,
    }
    form = ProductModelForm(data=form_data_2)
    assert form.is_valid()
    product_2 = form.save()

    product_from_db = Product.objects.get(id=product_1.id)
    assert product_1.name == product_from_db.name

    assert product_2.name == form_data_2["name"]

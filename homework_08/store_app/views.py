from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductModelForm, ProductDeleteForm


def index(request):
    return render(request, 'store_app/home.html')


def about(request):
    return HttpResponse("Testing Django. Otus Basic. Implementation of Store app.")


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store_app/product_list.html", context=context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "store_app/product_detail.html", context=context)


def add_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductModelForm()
    context = {
        'form': form,
        'title': 'Add product',
        'text': '',
        'btn_name': 'Add'
    }
    return render(request, 'store_app/crud_product.html', context=context)


def edit_product(request, product_id):
    product =get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductModelForm(instance=product)
    context = {
        'form': form,
        'title': 'Edit product',
        'text': '',
        'btn_name': 'Save'
    }
    return render(request, 'store_app/crud_product.html', context=context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            product.delete()
            return redirect('product_list')
    else:
        form = ProductDeleteForm()
    context = {
        'form': form,
        'title': 'Delete product',
        'text': f'Confirm to delete {product.name}?',
        'btn_name': 'Delete'
    }
    return render(request, 'store_app/crud_product.html', context=context)

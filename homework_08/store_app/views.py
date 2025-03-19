from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


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

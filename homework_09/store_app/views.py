from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView,
    RedirectView,
    View,
)
from django.contrib import messages
from .models import Category, Product
from .forms import ProductModelForm, ProductDeleteForm


def index(request):
    return render(request, "store_app/home.html")


class ProductListView(ListView):
    model = Product
    template_name = "store_app/product_list.html"
    context_object_name = "products"

    # Filtering
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get("category")
        max_price = self.request.GET.get("price")

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "store_app/product_detail.html"
    context_object_name = "product"

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.rating += 1  # how many times this page was open
        product.save()

        return super().get(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = "store_app/crud_product.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Product was created successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add product"
        context["btn_name"] = "Add"
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "store_app/crud_product.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Product was updated successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit product"
        context["btn_name"] = "Save"
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "store_app/crud_product.html"
    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["title"] = "Delete product"
        context["text"] = mark_safe(f"Confirm to delete <strong>{product.name}</strong>?")
        context["btn_name"] = "Delete"
        return context


class AboutTemplateView(TemplateView):
    template_name = "store_app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About"
        context["text"] = "Testing Django. OTUS Basic. Implementation of Store app."
        return context

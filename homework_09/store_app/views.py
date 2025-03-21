from django.shortcuts import render, get_object_or_404, redirect
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
    """
    Render the home page of the store application.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, "store_app/home.html")


class ProductListView(ListView):
    """
    Display a list of products with optional filtering by category and price.
    """
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
    """
    Display detailed information about a specific product.
    Increments the product's rating each time the page is viewed.
    """
    model = Product
    template_name = "store_app/product_detail.html"
    context_object_name = "product"

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.rating += 1  # how many times this page was open
        product.save()

        return super().get(request, *args, **kwargs)


class ProductCreateView(CreateView):
    """
    View for creating a new product.
    Displays a form and handles form submission.
    """
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
    """
    View for updating an existing product.
    Displays a form with current product data and handles form submission.
    """
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
    """
    View for deleting an existing product.
    Displays a confirmation page and handles product deletion.
    """
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
    """
    View for displaying the About page with general information about the app.
    """
    template_name = "store_app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About"
        context["text"] = "Testing Django. OTUS Basic. Implementation of Store app."
        return context

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.AboutTemplateView.as_view(), name="about"),
    path("product/", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/add/", views.ProductCreateView.as_view(), name="add_product"),
    path(
        "product/<int:pk>/edit", views.ProductUpdateView.as_view(), name="edit_product"
    ),
    path(
        "product/<int:pk>/delete",
        views.ProductDeleteView.as_view(),
        name="delete_product",
    ),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/<int:product_id>/edit', views.edit_product, name='edit_product'),
    path('product/<int:product_id>/delete', views.delete_product, name='delete_product'),
]

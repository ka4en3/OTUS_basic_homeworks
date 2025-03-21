from django.contrib import admin
from decimal import Decimal
from .models import Category, Product
from .forms import ProductModelForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Use custom form for the admin"""
    form = ProductModelForm
    list_display = ("name", "description", "price", "category", "created_at")
    ordering = ("name", "-price")
    list_filter = ("category", "price", "created_at")
    search_fields = ("name", "description")
    search_help_text = "Search by name or description"
    readonly_fields = ("created_at",)
    list_per_page = 25

    # fields = ("name", "price", "category")
    fieldsets = (
        ("Main options", {"fields": ("name", "category", "price")}),
        ("Advanced options", {"classes": ("collapse",), "fields": ("description",)}),
    )

    @admin.action(description="Indexing price")
    def indexing_price(self, request, queryset):
        for product in queryset:
            product.price = product.price * Decimal("1.1")
            product.save()
        self.message_user(request, "Prices were indexed.")

    actions = [indexing_price]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "product_count"]
    ordering = ["name"]
    search_fields = ["name", "description"]
    search_help_text = "Search by name or description"

    def product_count(self, obj):
        """Returns the number of products in this category"""
        return obj.products.count()

    product_count.short_description = "Products"

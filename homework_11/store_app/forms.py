from django import forms
import re
from .models import Product


class ProductModelForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.
    Provides custom validation and styling for product fields.
    """

    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]
        labels = {
            "name": "Product Name",
            "description": "Product Description",
            "price": "Price",
            "category": "Category",
        }
        help_texts = {
            "name": "Must be at least 2 characters long",
            "price": "Enter a value between 0.01 and 999",
            "category": "Select the appropriate category for this product",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter product name"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Enter product description",
                }
            ),
            "price": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter product price",
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        """
        Validate the product name field.
        Ensures the name is at least 2 characters long.
        Returns:
            str: The validated product name.
        Raises:
            ValidationError: If the name is less than 2 characters.
        """
        name = self.cleaned_data["name"]
        if len(name) < 2:
            raise forms.ValidationError(
                "Product name must be at least 2 characters long"
            )
        return name

    def clean_price(self):
        """
        Validate the product price field.
        Ensures the price is between 0.01 and 999.
        Returns:
            float: The validated price.
        Raises:
            ValidationError: If the price is outside the allowed range.
        """
        price = self.cleaned_data["price"]
        if float(price) < 0.01 or float(price) > 999:
            raise forms.ValidationError("Price must be between 0.01 and 999")
        return price

    def clean(self):
        """
        Perform cross-field validation for the entire form.
        Checks for excessive marketing buzzwords in description and
        validates the product name for special characters.
        Returns:
            dict: The cleaned form data.
        Raises:
            ValidationError: Added to specific fields if validation fails.
        """
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        price = cleaned_data.get("price")

        # Check description for common marketing buzzwords without substance
        if description:
            buzzwords = ["revolutionary", "innovative", "best", "perfect", "amazing"]
            buzzword_count = sum(1 for word in buzzwords if word in description.lower())

            if buzzword_count >= 3 and len(description) < 100:
                self.add_error(
                    "description",
                    "Description relies too heavily on marketing buzzwords. Please provide more specific details.",
                )

        # Check for special characters in the product name
        if name and re.search(r"[^a-zA-Z0-9\s\-_]", name):
            self.add_error(
                "name",
                "Product name should only contain letters, numbers, spaces, hyphens, and underscores",
            )

        return cleaned_data


class ProductDeleteForm(forms.Form):
    """
    Form for confirming product deletion.
    Provides a confirmation checkbox with a warning message.
    """

    confirm = forms.BooleanField(
        required=True,
        label="Confirm deletion",
        help_text="Warning: This action cannot be undone. All product data will be permanently removed.",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

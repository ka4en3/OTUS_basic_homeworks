from django.core.management.base import BaseCommand
from store_app.models import Category, Product
from faker import Faker


class Command(BaseCommand):
    help = "Generate test data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Generating test data...")

        faker = Faker()
        for _ in range(5):
            category = Category.objects.create(
                name=faker.word(),
                description=faker.text(),
            )
            if category:
                self.stdout.write(f"Category {category.name} created")

                for _ in range(5):
                    product_name = faker.word()
                    product_description = faker.text()
                    product_price = faker.random_number(digits=3)
                    product_category = category

                    product = Product.objects.create(
                        name=product_name,
                        description=product_description,
                        price=product_price,
                        category=product_category,
                    )
                    if product:
                        self.stdout.write(f"Product {product.name} created")

        self.stdout.write("Test data generated successfully.")

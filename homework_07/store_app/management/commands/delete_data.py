"""checking if cascade deleting works"""

from django.core.management.base import BaseCommand
from store_app.models import Category


class Command(BaseCommand):
    help = "Checking if cascade deleting works"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting some data...")

        category = Category.objects.all()
        category.first().delete()

        self.stdout.write("Delete was successful.")

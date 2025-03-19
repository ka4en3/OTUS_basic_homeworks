from django.apps import AppConfig
from django.db.backends.signals import connection_created


def enable_foreign_keys(sender, connection, **kwargs):
    """Enable foreign key constraints for SQLite."""
    if connection.vendor == "sqlite":
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.close()


class StoreAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store_app"

    def ready(self):
        # Connect the signal
        connection_created.connect(enable_foreign_keys)

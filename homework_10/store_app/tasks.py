from celery import shared_task
import eventlet


@shared_task
def add(x, y):
    eventlet.sleep(5)
    return x + y


@shared_task
def product_creation_logging(product_name, product_category):
    print(f"Product {product_name} in {product_category} was created successfully.")
    return "Task done"

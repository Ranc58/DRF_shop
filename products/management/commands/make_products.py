from django.core.management.base import BaseCommand
from products import factories


class Command(BaseCommand):
    help = 'Creates test products for development'

    product_items_count = 5

    def handle(self, *args, **options):
        for _ in range(self.product_items_count):
            factories.ProductsFactory.create()

from django.core.management.base import BaseCommand
from products import factories


class Command(BaseCommand):
    help = 'Creates test tags for development'

    tag_items_count = 5

    def handle(self, *args, **options):
        for _ in range(self.tag_items_count):
            factories.TagsFactory.create()
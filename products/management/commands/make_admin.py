from django.core.management.base import BaseCommand
from products import factories


class Command(BaseCommand):
    help = 'Creates test admin user for development.\n L: Admin P: adm1n'

    def handle(self, *args, **options):
        factories.UserFactory.create()
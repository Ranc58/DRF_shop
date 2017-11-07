import random
import factory
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .models import Tag


TAGS = [
        'Mobile phones', 'PC technic',
        'Technic for home', 'Technic for garage',
        'Technic for kitchen'
    ]

PRODUCTS = [
        'Apple iPhone SE', 'Apple MacBook PRO 2015',
        'icebox Samsung', 'Bosch ‎HD19-2',
        'Home cleaner Zanussi'
    ]


class UserFactory(factory.django.DjangoModelFactory):
    username = 'Admin'
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')
    is_superuser = True
    is_staff = True
    is_active = True

    class Meta:
        model = 'auth.User'


class TagsFactory(factory.DjangoModelFactory):
    title = factory.Iterator(TAGS)
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))

    class Meta:
        model = 'products.Tag'


class ProductsFactory(factory.DjangoModelFactory):
    title = factory.Iterator(PRODUCTS)
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    cost = factory.Faker('pyint')
    is_active = True
    added_by = User.objects.filter(username='Admin').first()

    @factory.post_generation
    def add_tags(self, create, extracted, **kwargs):
        self.tags.add(random.choice(Tag.objects.all()))

    class Meta:
        model = 'products.Product'

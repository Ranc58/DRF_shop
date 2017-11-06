from rest_framework import viewsets
from .filters import ProductFilter
from .models import Product, Tag
from .serializers import ProductSerializer, TagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    lookup_field = 'slug'


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


import django_filters
from .models import Product, Tag


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.ModelMultipleChoiceFilter(
        name='tags__slug',
        queryset=Tag.objects.all(),
        to_field_name='slug',
        conjoined=True,
    )

    class Meta:
        model = Product
        fields = ['title', 'tags']

from rest_framework import serializers
from .models import Tag, Product


class TagSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug',
    )

    class Meta:
        model = Tag
        fields = ('id', 'title', 'slug', 'url', 'products')
        read_only_fields = ('slug',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True, slug_field='slug',
        read_only=False,
        queryset=Tag.objects.all()
    )
    added_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Product
        fields = (
            'id', 'url', 'title', 'slug', 'is_active',
            'cost', 'tags', 'added_by'
        )
        read_only_fields = ('slug',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

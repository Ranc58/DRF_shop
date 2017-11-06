from django.template.defaultfilters import slugify
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(unique=True)
    cost = models.IntegerField(null=False)
    is_active = models.BooleanField(default=False)
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='products')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
from django.db import models


class Category(models.Model):
    """
    Returns category for the products
    """
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_color = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.name
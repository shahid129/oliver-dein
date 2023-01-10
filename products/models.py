from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Returns category for the products
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    Add comments to a product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order the Comments by recently created items first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
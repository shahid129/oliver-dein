from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'price', 'rating']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category)

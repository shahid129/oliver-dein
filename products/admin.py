from django.contrib import admin
from .models import Product, Category, Comment


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'price', 'rating']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment management section for admin
    """
    list_display = ('name', 'body', 'product', 'created_on', 'approved')


admin.site.register(Category)

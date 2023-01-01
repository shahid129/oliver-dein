from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Create a form of products
    """
    class Meta:
        model = Product
        fields = '__all__'

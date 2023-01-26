from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Comment


class ProductForm(forms.ModelForm):
    """
    Create a form of products
    """
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug',)
        abstract = True
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """
    Create a customer comment form
    """
    class Meta:
        """
        Available fields for customer comment form
        """
        model = Comment
        fields = ('name', 'body',)

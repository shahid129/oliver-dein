from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def products(request):
    """
    A view to return the index page
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """
    A view to show product details
    """
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
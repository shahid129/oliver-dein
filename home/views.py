from django.shortcuts import render
from products.models import Product
# Create your views here.


def index(request):
    """
    A view to return the index page
    """

    products = Product.objects.all()
    featured_products = products.order_by('-id')[:9]  # show recent 8 featured products
    recently_added = products.order_by('-id')[:9]  # show recently added  8 products
    context = {
        'products': products,
        'featured_products': featured_products,
        'recently_added': recently_added,
    }

    return render(request, 'home/index.html', context)

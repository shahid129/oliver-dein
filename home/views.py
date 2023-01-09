from django.shortcuts import render
from products.models import Product, Comment
# Create your views here.


def index(request):
    """
    A view to return the index page
    """

    products = Product.objects.all()
    featured_products = products.order_by('-id')[:8]  # show recent 8 featured products
    recently_added = products.order_by('-id')[:8]  # show recently added  8 products

    comments = Comment.objects.all().order_by('-id')[:10]
    context = {
        'products': products,
        'featured_products': featured_products,
        'recently_added': recently_added,
        'comments': comments
    }

    return render(request, 'home/index.html', context)

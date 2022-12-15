from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def products(request):
    """
    A view to return the index page
    """
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        # Get category items
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        # Get search items
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter your search criteria')
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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
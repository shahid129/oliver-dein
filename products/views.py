from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm, CommentForm

# Create your views here.


def products(request):
    """
    A view to return the index page
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Sort out products
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """
    A view to show product details
    """
    product = get_object_or_404(Product, slug=slug)
    comments = product.comments.filter(approved=True).order_by('-created_on')

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()

            messages.info(request, 'Waiting to be approved!')
            return redirect(reverse('product_detail', args=[product.slug]))
    else:
        comment_form = CommentForm()

    context = {
        'product': product,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only store owners are allowed here.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request, 'Failed to add product. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only store owners are allowed here.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(
                request, 'Failed to update product.\
                    Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_products.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, slug):
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only store owners are allowed here.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    product.delete()
    messages.success(request, f'{product.name} deleted!')
    return redirect(reverse('products'))

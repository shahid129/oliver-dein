from django.shortcuts import render, redirect, reverse, HttpResponse ,get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def bag(request):
    """
    A view to return the contents in the bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, slug):
    """ Add product quantity to shopping bag """

    product = get_object_or_404(Product, slug=slug)
    print(product.name)
    print(slug)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if slug in list(bag.keys()):
            if size in bag[slug]['items_by_size'].keys():
                bag[slug]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[slug]["items_by_size"][size]}')
            else:
                bag[slug]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[slug] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if slug in list(bag.keys()):
            bag[slug] += quantity
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[slug] = quantity
            messages.success(request, f'Added { product.name } to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, slug):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, slug=slug)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[slug]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[slug]["items_by_size"][size]}')
        else:
            del bag[slug]['items_by_size'][size]
            if not bag[slug]['items_by_size']:
                bag.pop(slug)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag') 
    else:
        if quantity > 0:
            bag[slug] = quantity
            messages.success(request, f'Updated { product.name } quantity to {bag[slug]} ')
        else:
            bag.pop(slug)
            messages.success(request, f'Removed { product.name } from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, slug):
    """Remove the item from  bag"""

    product = get_object_or_404(Product, slug=slug)


    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[slug]['items_by_size'][size]
            if not bag[slug]['items_by_size']:
                bag.pop(slug)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(slug)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

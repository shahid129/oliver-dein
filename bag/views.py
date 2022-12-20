from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def bag(request):
    """
    A view to return the contents in the bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, slug):
    """ Add product quantity to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if slug in list(bag.keys()):
            if size in bag[slug]['items_by_size'].items():
                bag[slug]['items_by_size'][size] += quantity
            else:
                bag[slug]['items_by_size'][size] = quantity
        else:
            bag[slug] = {'items_by_size': {size: quantity}}
    else:
        if slug in list(bag.keys()):
            bag[slug] += quantity
        else:
            bag[slug] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, slug):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[slug]['items_by_size'][size] = quantity
        else:
            del bag[slug]['items_by_size'][size]
            if not bag[slug]['items_by_size']:
                bag.pop(slug)
    else:
        if quantity > 0:
            bag[slug] = quantity
        else:
            bag.pop(slug)

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, slug):
    """Remove the item from  bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[slug]['items_by_size'][size]
            if not bag[slug]['items_by_size']:
                bag.pop(slug)
        else:
            bag.pop(slug)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

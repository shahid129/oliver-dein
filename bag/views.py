from django.shortcuts import render, redirect

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
    bag = request.session.get('bag', {})

    if slug in list(bag.keys()):
        bag[slug] += quantity
    else:
        bag[slug] = quantity

    return redirect(redirect_url)

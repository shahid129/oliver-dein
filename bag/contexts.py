from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    A function to check if the user can get free delivery 
    and total cost
    """
    bag_items = []
    total = 0
    product_count = 0

    # access the shopping bag
    bag = request.session.get('bag', {})

    for slug, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, slug=slug)
            if product.discount_price:
                total += item_data * product.discount_price
            else:
                total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'slug': slug,
                'quantity': item_data,
                'product': product
            })
        else:
            product = get_object_or_404(Product, slug=slug)
            for size, quantity in item_data['items_by_size'].items():
                if product.discount_price:
                    total += quantity * product.discount_price
                else:
                    total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'slug': slug,
                    'quantity': item_data,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery_charge = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery_charge = 0
        free_delivery_delta = 0

    grand_total = delivery_charge + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_charge': delivery_charge,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

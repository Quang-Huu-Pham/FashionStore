from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .cart import Cart
from product.models import Product
# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')


def clear_item(request, product_id):
    cart = Cart(request)
    cart.clear(product_id)
    return redirect('cart')


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(id=product_id)
    quantity = cart.get_item(product_id)['quantity']

    item = {
        'product': {
            'id': product.id,
            'image': product.image,
            'name': product.name,
            'price': product.price,
            'old_price': product.old_price,
        },
        'total_price': (quantity * product.price) / 1000,
        'quantity': quantity
    }

    response = render(request, 'cart/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def cart(request):
    return render(request, 'cart/cart.html')


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')


def hx_total_product(request):
    return render(request, 'cart/total_product.html')


def hx_total_all(request):
    return render(request, 'cart/total_all.html')

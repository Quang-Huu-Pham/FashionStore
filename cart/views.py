from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .cart import Cart
# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')


def remove(request, product_id):
    cart = Cart(request)
    cart.clear(product_id)
    return redirect('cart')


@login_required
def cart(request):
    return render(request, 'cart/cart.html')

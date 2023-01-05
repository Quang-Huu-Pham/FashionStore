from django.shortcuts import render, redirect

from cart.cart import Cart
from .models import Order, OrderItem

# Create your views here.


def start_order(request):
    cart = Cart(request)
    total_price = 0

    if request.method == 'POST':
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        for item in cart:
            product = item['product']
            total_price += product.price * int(item['quantity'])

        order = Order.objects.create(
            user=request.user,
            email=email,
            address=address,
            phone=phone,
            paid=True,
            paid_amount=total_price
        )

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(
                order=order, product=product, quantity=quantity, price=price)

        return redirect('myprofile')
    return redirect('cart')

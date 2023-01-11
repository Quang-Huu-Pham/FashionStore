from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

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

        subject = 'Fashion Store'
        content = 'Chào ' + str(order.user) + ' ! \nBạn đã đặt hàng thành công tại Fashion Store.\nTổng đơn hàng cần thanh toán là: ' + \
            str(int(order.paid_amount) + 20000) + \
            ' VND. Vui lòng thanh toán khi nhận hàng.\nCảm ơn ❤❤❤.'
        send_mail(subject, content, settings.EMAIL_HOST_USER,
                  [order.email], fail_silently=False)
        return redirect('myprofile')
    return redirect('cart')

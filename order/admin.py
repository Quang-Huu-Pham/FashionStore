from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'address',
                    'phone', 'created_at', 'paid', 'paid_amount']


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']


admin.site.register(OrderItem, OrderItemAdmin)

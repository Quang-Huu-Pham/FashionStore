from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders",
                             blank=True, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    def get_total_price(self):
        if self.paid_amount:
            return (self.paid_amount / 1000) + 20

        return 0


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.price / 1000

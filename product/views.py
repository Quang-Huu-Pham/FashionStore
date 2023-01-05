from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def product(request, id):
    product = get_object_or_404(Product, id=id)
    relates = Product.objects.all()[0:4]

    return render(request, 'product/product.html', {'product': product, 'reletes': relates})

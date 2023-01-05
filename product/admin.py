from django.contrib import admin

from .models import Category, Classify, Product
# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'image', 'name', 'slug',
                    'price', 'old_price', 'sale', 'created_at', 'classify']

    list_filter = ['category', 'slug']


admin.site.register(Category)
admin.site.register(Classify)
admin.site.register(Product, ProductAdmin)

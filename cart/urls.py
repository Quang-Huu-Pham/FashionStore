from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/',
         views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.clear_item, name='remove'),
    path('update_cart/<int:product_id>/<str:action>/',
         views.update_cart, name='update_cart'),
    path('hx_menu_cart/', views.hx_menu_cart, name='hx_menu_cart'),
    path('hx_total_product/', views.hx_total_product, name='hx_total_product'),
    path('hx_total_all/', views.hx_total_all, name='hx_total_all'),
]

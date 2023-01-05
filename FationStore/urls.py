from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cart.views import cart

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('', include('cart.urls')),
    path('order/', include('order.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

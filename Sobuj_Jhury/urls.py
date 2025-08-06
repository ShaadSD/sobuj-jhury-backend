from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('product.urls')),
    path('cart/',include('cart.urls')),
    path('user/',include('user.urls')),
    path('order/',include('orders.urls')),
    path('review/',include('reviews.urls'))
]

from django.urls import path,include

from .views import AddToCart,UpdateCartProduct,EditCartProduct,DeleteCartProduct,MyCart


urlpatterns = [
    path('add-to-cart/<int:id>/',AddToCart.as_view(),name = 'add-to-cart'),
    path('update_cart/<int:id>/',UpdateCartProduct.as_view(),name = 'update_cart'),
    path('edit_cart/<int:id>/',EditCartProduct.as_view(),name = 'edit_cart'),
    path('delete_cart/<int:id>/',DeleteCartProduct.as_view(),name = 'delete_cart'),
    path('list_cart/',MyCart.as_view(),name = 'list_cart'),
]




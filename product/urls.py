from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewset





router = DefaultRouter()
router.register('list',ProductViewSet,basename='list')
router.register('category',CategoryViewset,basename='category')

urlpatterns = [
    path('',include(router.urls)),
]


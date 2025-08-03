from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Product,Category
from .serializers import ProductSerializers,CategorySerializers
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in  SAFE_METHODS:
            return True

        return request.user and request.user.is_staff


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__slug',lookup_expr='iexact')
    min_price = django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price',lookup_expr='lte')

    class Meta:

        model = Product
        fields = ['available', 'category','min_price','max_price']





class ProductPagination(PageNumberPagination):
    page_size=10
    page_size_query_param = page_size
    max_page_size=100




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    pagination_class = ProductPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['name','description','category__name']
    ordering_fields = ['price']
    ordering = ['price']




class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
from rest_framework import serializers
from .models import Product,Category

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'slug', 'description', 'price', 'Old_price', 'discount', 'unit', 'image', 'available']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
from rest_framework import serializers
from .models import Product,Category

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    image = serializers.SerializerMethodField()

    def get_image(self,obj):
        if obj.image:
            return obj.image.url
        return None
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'slug', 'description', 'price', 'Old_price', 'discount', 'unit', 'image', 'available']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
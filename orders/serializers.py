from rest_framework import serializers
from .models import Order
from .models import Country, District, Upazila

class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upazila
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    upazilas = UpazilaSerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'upazilas']


class CountrySerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'districts']
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



from rest_framework.views import APIView
from product.models import Product
from .models import Order,District,Upazila,Country
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import OrderSerializer
from .serializers import CountrySerializer, DistrictSerializer, UpazilaSerializer

class ConfirmOrderAPIView(APIView):
    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        quantity = int(request.data.get("quantity", 1))

   
        shipping = 100
        subtotal = product.price * quantity
        total = subtotal + shipping

  
        phone = request.data.get("phone_number")
        alt_phone = request.data.get("alternative_phone_number")
        full_address = request.data.get("full_address")

        country_id = request.data.get("country_id")
        district_id = request.data.get("district_id")
        upazila_id = request.data.get("upazila_id")


        Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            price=product.price,
            subtotal=total,
            shipping=shipping,
            phone_number=phone,
            alternative_phone_number=alt_phone,
            full_address=full_address,
            country_id=country_id,
            district_id=district_id,
            upazila_id=upazila_id
        )

        return Response({
            "success": True,
            "message": "Order confirmed successfully",
            "product": product.name,
            "quantity": quantity,
            "subtotal": subtotal,
            "shipping": shipping,
            "total": total
        })
    


class OrderCalculationAPIView(APIView):
    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        quantity = int(request.data.get("quantity", 1))


        shipping = 100
        subtotal = product.price * quantity
        total = subtotal + shipping

        return Response({
            "product": product.name,
            "unit_price": product.price,
            "quantity": quantity,
            "subtotal": subtotal,
            "shipping": shipping,
            "total": total
        })   
    



class OrderList(APIView):
    
    def get(self,request):
        allord = Order.objects.filter(user = request.user)
        serializer = OrderSerializer(allord,many = True)

        return Response(serializer.data)
    


class CountryListAPIView(APIView):
    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class DistrictListAPIView(APIView):
    def get(self, request, country_id):
        districts = District.objects.filter(country_id=country_id)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)


class UpazilaListAPIView(APIView):
    def get(self, request, district_id):
        upazilas = Upazila.objects.filter(district_id=district_id)
        serializer = UpazilaSerializer(upazilas, many=True)
        return Response(serializer.data)
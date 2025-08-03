from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReviewSerializers
# Create your views here.
from rest_framework.views import APIView
from .models import Review
from product.models import Product
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

class RevView(APIView):
    def post(self,request,id):
        product = get_object_or_404(id=id)
        data = {
            "reviewer": request.user.id,
            "product": product.id,
            "body": request.data.get("body"),
            "rating": request.data.get("rating")
        }

        serializer = ReviewSerializers(data,many = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)

        return Response(serializer.errors, status = 400)



    def get(self,request,id):
        pro = Product.objects.get(id = id)
        rev = Review.objects.filter(product = pro, reviewer = request.user)
        serializer = ReviewSerializers(rev,many =True)
        return Response (serializer.data)
    
    def delete(self,request,id):
        rev_id = Review.objects.get(id=id)
        rev_id.delete()
        return Response("Review Delete")


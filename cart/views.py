from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Cart,CartItem
from product.models import Product
from rest_framework.response import Response
from .serializers import CartSerializers,CartItemSerializers
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class MyCart(ListAPIView):
     serializer_class = CartItemSerializers
     def get_queryset(self):
            Cart_pro = Cart.objects.get(user = self.request.user)
            item_pro = CartItem.objects.filter(cart = Cart_pro)
            return item_pro


class AddToCart(APIView):
   
    def post(self,request,id):
        product = Product.objects.get(id=id)
        cart_cart = Cart.objects.filter(user = request.user).first()

        if cart_cart:
            itemcart = CartItem.objects.filter(cart=cart_cart, product= product)
            
            if itemcart.exists():
                itemcart1 = CartItem.objects.filter(product=product,cart=cart_cart).first()
                itemcart1.quantity+=1
                itemcart1.subtotal+=product.price
                itemcart1.save()
                cart_cart.total+=product.price
                cart_cart.save()
                return Response({'error':False,'message':'cart item succesfullly'})
            else:
                cart_new=CartItem.objects.create(
                    cart = cart_cart,
                    # product = product,
                    price = product.price,
                    quantity = 1,
                    subtotal = product.price
                )
                cart_new.product.add(product)
       
                cart_cart.total+=product.price
                cart_cart.save()

                return Response({'error':False,'message':'cart item succesfullly'})
        else:
            cart_cart = Cart.objects.create(user=request.user , total = 0)

            new_create = CartItem.objects.create(
                cart = cart_cart,
                # product = product,
                price = product.price,
                quantity = 1,
                subtotal = product.price
            )
            new_create.product.add(product)
            new_create.save()
            cart_cart.total+=product.price
            cart_cart.save()

            return Response({'error':False,'message':'cart item succesfullly'})
        
        return Response({'error':True,'message':'cart item not succesfullly'})
       
        

class UpdateCartProduct(APIView):
    def post(self,request,id):
        cp_obj = CartItem.objects.get(id=id)
        pro_obj = cp_obj.cart
        cp_obj.quantity+=1
        cp_obj.subtotal+=cp_obj.price
        cp_obj.save()
        pro_obj.total+=cp_obj.price
        pro_obj.save()
        return Response({"message": "Cart item updated successfully", "cart_item_id": id})

class EditCartProduct(APIView):
    def post(self,request,id):
        cp_obj = CartItem.objects.get(id =id)
        pro_obj = cp_obj.cart
        cp_obj.quantity-=1
        cp_obj.subtotal-=cp_obj.price
        cp_obj.save()
        pro_obj.total-=cp_obj.price
        pro_obj.save()
        return Response({"messsage":"Cart item update successfully","cart_item_id":id})

class DeleteCartProduct(APIView):
     def post(self,request,id):
         ite_pro = CartItem.objects.get(id=id)
         ite_cart = ite_pro.cart
         ite_pro.delete()
         return Response({"messsage":"Cart item Deleted","cart_item_id":id})
        
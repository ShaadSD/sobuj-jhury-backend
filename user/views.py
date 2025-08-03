from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from rest_framework.response import Response
from .models import Profile
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.permissions import BasePermission,SAFE_METHODS,IsAuthenticated,AllowAny
from .serializers import UserSerializer,UserProfileSerializers,UserLoginSerializers,RegistrationSerializer,PasswordChangeSerializer
# Create your views here.

class IsAdminAndStaff(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_staff or user.is_superuser:
            if request.method in SAFE_METHODS or request.method in ['POST','PATCH','PUT','DELETE']:
                return True
        
        return False

        


class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminAndStaff]

class UserProfileList(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [IsAdminAndStaff]

class UserProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializers

    def get_object(self):
        return Profile.objects.get(user = self.request.user)

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = RegistrationSerializer(data = request.data)
        email = request.data.get('email')
        if User.objects.filter(email=email).exists(): 
            return Response({'error':"Email Already exist"},status = 400)
        if serializer.is_valid():
            user = serializer.save()
            email_subjects = "Sign Up Successfully"
            email_body = render_to_string('sign_up.html')
            email = EmailMultiAlternatives(email_subjects,'',to = [user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response({'message': "Your sign up complete check email"},status=200)

        return Response(serializer.errors,status=400)




class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username , password = password)
            if user:
                token,_ = Token.objects.get_or_create(user =user)
                login(request,user)
                request.session['user_id']=user.id 
                return Response({'token':token.key,'user_id':user.id})
            else:
                return Response({'error':"Invalid Credentials"})
        return Response(serializer.errors)




class LogoutView(APIView):
    def get(self,request):
        logout(request)
        return Response({'message':"Log out Successfully"},status=200)
        

class PasswordChangeView(APIView):
    def post(self,request):
        serializer = PasswordChangeSerializer(data = self.request.data,context= {'request':request})

        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Password Change Successfully and check email"},status=200)
        
        return Response(serializer.errors,status=400)
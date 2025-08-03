from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
class UserProfileSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields ='__all__'

    def get_username(self,obj):
        return obj.user.username
    def get_first_name(self,obj):
        return obj.user.first_name
    def get_last_name(self,obj):
        return obj.user.last_name
        
    def get_email(self,obj):
        return obj.user.email

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','first_name','email','last_name','password','confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password!=password2 :
            raise serializers.ValidationError({'error':"Password does not match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already Exists"})
        
        account= User(username = username,email=email,first_name=first_name,last_name = last_name)
        account.set_password(password)
        account.is_active=True
        account.save()
        Profile.objects.create(user = account)
        return account

class UserLoginSerializers(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    confirm_new_password = serializers.CharField(required = True)

    def validate(self, data):
        if data['new_password']!=data['confirm_new_password']:
            raise serializers.ValidationError("new password do not match")
        return data
    
    def validate_old_password(self,value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password not corrected")
        return value
    
    def save(self,**kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        self.send_confirmation_email(user.email)
        return user

    def send_confirmation_email(self,email):
        subject = 'Password Change Confirmation'
        message = 'Your password has been successfully changed.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)  

    
        
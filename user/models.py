from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)
    mobile_no = models.CharField(max_length=15,blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


from django.db import models
from django.contrib.auth.models import User
from product.models import Product

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    shipping = models.IntegerField()
    subtotal = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="Order Received")
    phone_number = models.CharField(max_length=20)
    alternative_phone_number = models.CharField(max_length=20, null=True, blank=True)
    full_address = models.TextField()
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    upazila = models.ForeignKey('Upazila', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.country.name})"


class Upazila(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, related_name='upazilas', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.district.name})"
    




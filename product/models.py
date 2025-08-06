from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    category=models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField()
    Old_price = models.IntegerField()
    discount = models.IntegerField()
    unit = models.DecimalField(max_digits=12,decimal_places=3,blank = True,null=True)
    image = models.URLField(max_length=200,blank=True, null=True)
    available = models.BooleanField()

    def __str__(self):
        return self.name
from django.contrib import admin
from .models import Cart,CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['first_name','total','date']
    def first_name(self,obj):
        return obj.user.first_name
    

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
from django.contrib import admin

from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','unit','available','Old_price','discount','description']
    prepopulated_fields = {"slug": ("name",)} 


    def description(self,obj):
        return obj.description[:20]
    
    description.short_description="Description"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Product, Category,Customer,Order
# Register your models here.

class Product_List(admin.ModelAdmin):
    list_display = ('name','price','category')


class Category_List(admin.ModelAdmin):
    list_display = ['name']
class Customer_List(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','password')

admin.site.register(Product, Product_List)
admin.site.register(Category,Category_List)
admin.site.register(Customer,Customer_List)
admin.site.register(Order)

from django.contrib import admin
from store.models import Category, Color, Product, SubCategory, Size, Customer, Order, OrderItem, ShippingAddress, Cart

# Register your models here.


admin.site.register([Category, Color, Product, SubCategory, Size, Customer, Order, OrderItem, ShippingAddress, Cart])
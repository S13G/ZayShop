from django.contrib import admin
from store.models import Category, Color, Product, SubCategory, Size

# Register your models here.


admin.site.register([Category, Color, Product, SubCategory, Size])
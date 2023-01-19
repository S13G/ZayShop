from django.contrib import admin
from store.models import Category, Product, SubCategory

# Register your models here.


admin.site.register([Category, Product, SubCategory])
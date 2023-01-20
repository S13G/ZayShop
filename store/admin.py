from django.contrib import admin
from store.models import Category, Product, SubCategory, Size

# Register your models here.


admin.site.register([Category, Product, SubCategory, Size])
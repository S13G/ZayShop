from django.shortcuts import render
from store.models import Category, Product

# Create your views here.


def products(request):
    categories = Category.objects.all()
    all_products = Product.objects.all()
    print(all_products.values_list('sizes', flat=True))
    context = {"categories": categories, "products": all_products}
    return render(request, "store/shop.html", context)
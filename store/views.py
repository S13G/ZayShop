from django.shortcuts import render
from store.models import Category, Product
from store.utils import paginate_products
# Create your views here.


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    # pagination
    products, custom_range = paginate_products(request, products, 9)
    context = {"categories": categories, "products": products, "custom_range": custom_range}
    return render(request, "store/shop.html", context)
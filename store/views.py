from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages

from store.models import Category, Product, SubCategory
from store.utils import paginate_products


# Create your views here.


def display_products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    # pagination
    products, custom_range = paginate_products(request, products, 9)
    context = {"categories": categories, "products": products, "custom_range": custom_range}
    return render(request, "store/shop.html", context)


def products_filter(request, slug):
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    try:
        sub_category = sub_categories.get(slug=slug)
    except SubCategory.DoesNotExist:
        messages.info(request, "Category does not exist")
        return redirect('products')
    sub_products = sub_category.products.all()
    if not sub_products.exists():
        messages.info(request, "No products in this category")
        return redirect('products')
    context = {"categories": categories, "sub_products": sub_products}
    return render(request, "store/products_filter.html", context)

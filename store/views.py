import random
import string

from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower, Substr
from django.shortcuts import render, redirect

from store.forms import DetailForm
from store.models import Category, Product, SubCategory
from store.utils import paginate_products


# Create your views here.


def display_products(request):
    categories = Category.objects.all()
    products = Product.selected.all()
    if not (categories and products):
        messages.error(request, "No products available in the shop")
        return redirect('home')
    # pagination
    products, custom_range = paginate_products(request, products, 9)
    context = {"categories": categories, "products": products, "custom_range": custom_range}
    return render(request, "store/shop.html", context)


def products_filter(request, slug):
    page = 'all'
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
    context = {"categories": categories, "sub_products": sub_products, "page": page}
    return render(request, "store/products_filter.html", context)


def filter_products_by_men(request):
    page = 'men'
    categories = Category.objects.all()
    men_products = Product.selected.filter(gender="M")
    if not men_products.exists():
        messages.info(request, "No products in this category")
        return redirect('products')
    context = {"categories": categories, "men_products": men_products, "page": page}
    return render(request, "store/products_filter.html", context)


def filter_products_by_women(request):
    page = 'women'
    categories = Category.objects.all()
    women_products = Product.selected.filter(gender="F")
    if not women_products.exists():
        messages.info(request, "No products in this category")
        return redirect('products')
    context = {"categories": categories, "women_products": women_products, "page": page}
    return render(request, "store/products_filter.html", context)


def featured_products(request):
    page = 'featured'
    categories = Category.objects.all()
    featured = Product.selected.filter(featured=True)
    if not featured:
        messages.info(request, 'No featured product')
        return redirect('products')
    context = {"categories": categories, "featured": featured, "page": page}
    return render(request, "store/products_filter.html", context)


def filter_products_by_letter(request):
    page = 'letters'
    uppercase_alphabet = string.ascii_uppercase
    categories = Category.objects.all()
    letters = Product.selected.order_by("name").annotate(first_letter=Lower(Substr('name', 1, 1)))
    letters = letters.exclude(~Q(first_letter__in=uppercase_alphabet))
    if not letters:
        messages.info(request, 'No product')
        return redirect('products')
    context = {"categories": categories, "letters": letters, "page": page}
    return render(request, "store/products_filter.html", context)


def single_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        messages.info(request, 'Product does not exist')
        return redirect('products')
    related_products = Product.selected.exclude(name=product.name)
    count = 16
    if related_products.count() < 6:
        count = related_products.count()
    related_products = random.sample(list(related_products), count)
    if request.method == "POST" and "buy-btn" in request.POST:
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item bought")
            return redirect(f'/store/product/{product.slug}/')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            messages.info(request, "Failed to make request")
            return redirect(f'/store/product/{product.slug}/')
    elif request.method == "POST" and "cart-btn" in request.POST:
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item added to cart successfully")
            return redirect(f'/store/product/{product.slug}/')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            messages.info(request, "Failed to add item to cart")
            return redirect(f'/store/product/{product.slug}/')
    else:
        form = DetailForm()
    context = {'product': product, "related_products": related_products, "form": form}
    return render(request, "store/shop-single.html", context)

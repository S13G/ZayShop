from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect

from store.models import Category, SubCategory


# this function paginates products
def paginate_products(request, products, results):
    page = request.GET.get("page")
    paginator = Paginator(products, results)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    # determines how many pagination numbers will be displayed

    left_index = (int(page) - 2)
    right_index = (int(page) + 3)

    if left_index < 1:
        left_index = 1
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return products, custom_range

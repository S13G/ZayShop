from django.shortcuts import render
from store.models import Category

# Create your views here.


def products(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "store/shop.html", context)
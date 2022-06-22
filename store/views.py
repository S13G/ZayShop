from django.views.generic import TemplateView

from store.models import Product


class MainPage(TemplateView):
    template_name = "index.html"


class ProductList(TemplateView):
    template_name = "shop.html"

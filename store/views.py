from django.views.generic import ListView

from store.models import Product


class ProductView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

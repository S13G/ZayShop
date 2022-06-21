from django.urls import path

from store.views import ProductView

urlpatterns = [
    path('products/', ProductView.as_view(), name="products")
]
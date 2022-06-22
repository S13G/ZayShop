from django.urls import path

from store.views import MainPage, ProductList

urlpatterns = [
    path('', MainPage.as_view(), name="main_page"),
    path('products/', ProductList.as_view(), name="product_list")
]
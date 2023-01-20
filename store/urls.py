from django.urls import path

from store import views

urlpatterns = [
    path('', views.products, name="products")
]

from django.urls import path

from store import views

urlpatterns = [
    path('', views.display_products, name="products"),
    path('products/<slug:slug>/', views.products_filter, name="products_filter"),
]

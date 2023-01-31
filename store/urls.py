from django.urls import path

from store import views

urlpatterns = [
    path('', views.display_products, name="products"),
    path('products/<slug:slug>/', views.products_filter, name="products_filter"),
    path('men-products/', views.filter_products_by_men, name="men_products"),
    path('women-products/', views.filter_products_by_women, name="women_products"),
    path('featured-products/', views.featured_products, name="featured_products"),
    path('product-letters/', views.filter_products_by_letter, name="product_letters"),
]

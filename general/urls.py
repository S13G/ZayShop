from django.urls import path
from general import views

urlpatterns = [
    path('', views.newsletter)
]
from django.urls import path

from store.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name="main_page")
]
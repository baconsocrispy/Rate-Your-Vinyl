from django.urls import path
from . import views


urlpatterns = [
    path('', views.crypto_home, name='Crypto_Home'),
]

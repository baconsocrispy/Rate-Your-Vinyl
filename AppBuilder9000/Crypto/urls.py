from django.urls import path
from . import views


urlpatterns = [
    path('', views.crypto_home, name='Crypto_Home'),
    path('AddCrypto/', views.crypto_addcrypto, name='crypto_add_crypto'),
]

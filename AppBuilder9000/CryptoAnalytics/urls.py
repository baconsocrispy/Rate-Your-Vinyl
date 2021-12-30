from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='crypto_home'),
    path('register', views.register, name='crypto_register'),
    path('about', views.about, name='crypto_about'),
]

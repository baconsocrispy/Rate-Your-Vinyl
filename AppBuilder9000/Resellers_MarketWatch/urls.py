from django.urls import path

from . import views

urlspatterns = [
    path('', views.MarketWatch_home, name='MarketWatch_home'),
]
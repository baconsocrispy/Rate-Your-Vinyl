from django.urls import path

from . import views

urlpatterns = [
    path('', views.MarketWatch_home, name='MarketWatch_home'),
]
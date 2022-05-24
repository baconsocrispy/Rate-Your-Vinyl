from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('PortfolioIndex', views.PortfolioIndex, name='PortfolioIndex'),
    path('Portfolio/navbar.html', views.navbar, name="navbar"),
]

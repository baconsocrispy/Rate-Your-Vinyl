from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.PortfolioIndex, name='PortfolioIndex'),
    path('Portfolio/navbar.html', views.navbar, name="navbar"),
    path('Portfolio_data.html', views.inqurieslist, name="Portfolio_data"),
    path('<int:pk>/portfolio_details', views.inquriesdetails, name="portfolio_details")
]

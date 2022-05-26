from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.PortfolioIndex, name='PortfolioIndex'),
    path('Portfolio/navbar.html', views.navbar, name="navbar"),
    path('Portfolio_data.html', views.inqurieslist, name="Portfolio_data"),
    path('<int:pk>/Portfolio_display.html', views.inquiry, name="inquiry_display"),
    path('<int:pk>/portfolio_details', views.inquriesdetails, name="inquiry_details"),
    path('<int:pk>/portfolio_delete/', views.inquirydelete, name='inquiry_delete'),
    path('portfolio_weather.html', views.weather_api, name='weather'),
]

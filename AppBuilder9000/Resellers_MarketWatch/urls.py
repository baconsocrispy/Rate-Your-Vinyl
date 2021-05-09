from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='MarketWatch_home'),
    path('AccountPage/', views.account, name='Account'),
    path('Register/', views.register, name='Register'),
    path('Listview/', views.all_webscrape, name='Listview'),
]
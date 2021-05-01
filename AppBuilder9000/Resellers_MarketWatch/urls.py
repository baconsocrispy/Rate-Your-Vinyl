from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Resellers_MarketWatch/AccountPage/', views.account, name='Account'),
    path('Resellers_MarketWatch/Register/', views.register, name='Register'),
]
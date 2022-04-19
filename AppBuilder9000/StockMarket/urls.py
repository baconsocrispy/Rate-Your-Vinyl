from django.urls import path
from . import views

urlpatterns = [
    path('', views.StockMarketHome, name='StockMarketHome'),
    path('create/', views.create_account, name='create'),

]
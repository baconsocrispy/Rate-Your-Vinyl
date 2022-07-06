from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='inventory_home'),
    path('create/', views.inventory_create, name='inventory_create'),
]
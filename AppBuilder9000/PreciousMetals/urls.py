from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name='PreciousMetals_home'),
    path('inventory', views.inventory, name='PreciousMetals_inventory'),
]
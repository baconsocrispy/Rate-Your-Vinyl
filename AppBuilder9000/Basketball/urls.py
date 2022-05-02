from django.urls import path
from . import views

urlpatterns = [
    path('', views.basketballHome, name='Basketball_Home'),
    path('pickup', views.basketballPickup, name='Pickup_Games'),
]

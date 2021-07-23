from django.urls import path, include
from . import views

urlpatterns = [
path('home/', views.home, name='TravelDestinations_home.html'),
path('add/', views.TravelDestinations_add, name='TravelDestinations_add.html'),
]

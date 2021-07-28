from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='TravelDestinations_home.html'),
    path('add/', views.TravelDestinations_add, name='TravelDestinations_add.html'),
    path('destinations/', views.destinations, name='TravelDestinations_destinations.html'),
    path('details/<int:id>/', views.tripDetails, name='TravelDestinations_details.html'),
]

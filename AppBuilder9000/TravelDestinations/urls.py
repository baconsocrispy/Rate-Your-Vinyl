from django.urls import path
from . import views

urlpatterns = [
    path('', views.TravelDestinationshome, name='TravelDestinations_home'),
    path('TravelDestinations_add/', views.TravelDestinationsadd, name='TravelDestinations_add')
]
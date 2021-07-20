from django.urls import path, include
from TravelDestinations import views

urlpatterns = [
path('', views.home, name='TravelDestinations_home.html'),
]

from django.urls import path, include
from SciFiWatchlist import views

urlpatterns = [
    path('SciFi-home/', views.SciFihome, name='SciFi-Home'),
    path('Add-Movies/', views.AddMovies, name='Add-Movies'),
    ]
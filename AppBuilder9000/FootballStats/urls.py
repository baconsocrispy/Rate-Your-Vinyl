from django.urls import path
from . import views

urlpatterns = [
    path('', views.footballstatshome, name='football_stats_home'),
    path('football_create/', views.add_player_stats, name='football_create'),
    ]
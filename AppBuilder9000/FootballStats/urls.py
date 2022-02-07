from django.urls import path
from . import views

urlpatterns = [
    path('', views.footballstatshome, name='football_stats_home'),
    path('football_create/', views.add_player_stats, name='football_create'),
    path('football_stats/', views.stats, name='football_stats'),
    path('<int:pk>/details/', views.player_details, name='football_stats_details'),
#    path('football_search/', views.search, name='football_search'),
    ]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='basketball_stats_home'),
    path('add_player/', views.create_player, name='basketball_stats_create'),
    path('players/', views.player_stats, name='basketball_stats_players'),
    path('<int:pk>/details/', views.player_details, name='basketball_stats_details'),
]

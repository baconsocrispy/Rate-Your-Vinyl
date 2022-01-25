from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='basketball_stats_home'),
    path('add_player/', views.create_player, name='basketball_stats_create'),
    path('players/', views.player_stats, name='basketball_stats_players'),
    path('<int:pk>/details/', views.player_details, name='basketball_stats_details'),
    path('<int:pk>/edit/', views.player_edit, name='basketball_stats_edit'),
    path('<int:pk>/delete', views.player_delete, name='basketball_stats_delete'),
    path('standings/', views.standings_page, name='basketball_stats_standings'),
    path('history/', views.history_scraping, name='basketball_stats_history'),
    path('bball_ref/', views.web_scraping, name='basketball_stats_web_scraping'),
    path('balldontlie/', views.ball_dont_lie, name='basketball_stats_bdl_api'),
    path('save_favorites/', views.save_favorites, name='basketball_stats_save_favorites'),
]

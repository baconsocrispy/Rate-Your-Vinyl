from django.urls import path
from . import views

urlpatterns = [
    path('', views.speed_run_home, name='speed_run_home'),
    path('speed_run_create/', views.add_record, name='speed_run_create'),
    path('speed_run_create_game/', views.add_game, name='speed_run_create_game'),
    path('speed_run_all_games/', views.all_games, name='speed_run_all_games'),
    path('speed_run_game_records/<int:pk>', views.game_record, name='speed_run_game_records'),
    path('speed_run_details/<int:pk>', views.speed_run_details, name='speed_run_details'),
]

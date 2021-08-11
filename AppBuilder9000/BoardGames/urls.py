from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardGames_home, name='BoardGames_home'),
    path('games/', views.BoardGames_games, name='BoardGames_games'),
    path('create/', views.BoardGames_create, name='BoardGames_create'),
    path('<int:pk>/game/', views.BoardGames_game, name='BoardGames_game'),
]

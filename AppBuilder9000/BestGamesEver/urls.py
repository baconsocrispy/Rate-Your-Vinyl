from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BestGamesEver_Home, name='BestGamesEver_Home'),
    path('GameCreate/', views.Game_Create, name='Game_Create'),
    path('ViewGames/', views.Game_View, name='Game_View'),
    path('<game_id>/details/', views.Game_Details, name='Game_Details'),
    path('<game_id>/edit/', views.Edit_Games, name='Edit_Games'),
    path('<game_id>/delete/', views.Delete_Games, name='Delete_Games'),
    path('<game_id>/price/', views.View_Price, name='View_Price'),



]
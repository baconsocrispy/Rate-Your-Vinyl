from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="gamestats_home"),
    path('add_game', views.add_game, name="gamestats_form"),
    path('view_games', views.view_games, name="gamestats_viewall"),
    path('<int:pk>/details/', views.game_details, name="gamestats_one"),
    path('<int:pk>/edit/', views.game_edit, name="gamestats_edit"),
    path('<int:pk>/delete/', views.game_delete, name="gamestats_delete"),
]
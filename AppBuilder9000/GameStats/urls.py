from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="gamestats_home"),
    path('add_game', views.add_game, name="gamestats_form"),
    path('view_games', views.view_games, name="gamestats_viewall")
]
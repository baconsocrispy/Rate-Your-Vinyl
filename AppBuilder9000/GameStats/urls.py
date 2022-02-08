from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="gamestats_home"),
    path('add_game', views.addgame, name="gamestats_form"),
]
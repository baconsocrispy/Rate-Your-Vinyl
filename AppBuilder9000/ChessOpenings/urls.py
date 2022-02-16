from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.homepage, name='chess_home'),
    path('chess_search', views.search_games, name="chess_search"),
    path('add_game/', views.add_game, name="add_game"),
]
urlpatterns += staticfiles_urlpatterns()

from django.urls import path, include
from . import views
from .views import MusicAlbums_home

urlpatterns = [
    path('', views.MusicAlbums_home, name='MusicAlbums_home' ),

]
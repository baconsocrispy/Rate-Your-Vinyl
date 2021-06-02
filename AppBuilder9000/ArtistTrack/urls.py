from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.at_home, name='at_home'),
    path('add_song', views.add_song, name='add_song'),
    path('add_playlist', views.add_playlist, name='add_playlist'),
]
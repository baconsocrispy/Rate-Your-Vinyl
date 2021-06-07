from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('at_home', views.at_home, name='at_home'),
    path('add_song', views.add_song, name='add_song'),
    path('add_playlist', views.add_playlist, name='add_playlist'),
    path('library', views.at_library, name='at_library'),
    path('<int:pk>/details', views.at_details, name='at_details'),
    path('<int:pk>/delete', views.at_delete, name='at_delete'),
    path('at_api', views.at_api, name='at_api'),
]

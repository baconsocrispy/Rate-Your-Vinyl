from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('AddShow/', views.add_show, name='AddShow'),
    path('ViewShows/', views.view_shows, name='ViewShows'),
]

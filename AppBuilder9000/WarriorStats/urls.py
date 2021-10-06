from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_Home, name='stats_Home'),
    path('addPlayer/', views.add_player, name='add_player'),
]
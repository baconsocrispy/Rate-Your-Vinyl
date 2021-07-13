from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from NBAstats import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.nba_home, name="stats-home")
    ]

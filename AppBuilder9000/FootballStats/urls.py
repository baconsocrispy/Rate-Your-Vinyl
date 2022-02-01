from django.urls import path
from . import views

urlpatterns = [
    path('', views.footballstatshome, name='football_stats_home'),
    ]
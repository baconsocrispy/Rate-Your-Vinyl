from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='basketball_stats_home'),
    path('add_player/', views.create_player, name='basketball_stats_create'),
]

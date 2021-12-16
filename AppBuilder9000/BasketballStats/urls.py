from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='basketball_stats_home'),
]

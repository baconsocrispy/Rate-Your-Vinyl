from django.urls import path
from . import views

urlpatterns = [
    path('', views.HikingTrails_home, name='HikingTrails_home'),
    path('HikingTrails_create', views.HikingTrails_create, name='HikingTrails_create'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HikingTrails_home, name='HikingTrails_home'),
]
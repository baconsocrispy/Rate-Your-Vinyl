from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_home, name='weather_home'),
    path('weathercreate/', views.weather_create, name='weather_create'),
]
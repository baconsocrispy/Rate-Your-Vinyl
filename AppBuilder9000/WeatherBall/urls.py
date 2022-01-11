from django.urls import path
from . import views

urlpatterns = [
    path('WeatherBall/', views.weather_home),
]
from django.urls import path
from . import views

urlpatterns = [
    path('WeatherBall/weatherhome.html', views.weather_home),
]
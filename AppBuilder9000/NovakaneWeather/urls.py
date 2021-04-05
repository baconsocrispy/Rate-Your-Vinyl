from django.urls import path
from . import views


urlpatterns = [
    path('', views.novakane_home, name="novakane_home"),
    path('Weather/', views.weather, name="weather"),
    path('Radar/', views.radar, name="radar"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_home, name='weather_home'),
    path('weathercreate/', views.weather_create, name='weather_create'),
    path('weatherdisplaydb/', views.weather_db, name='weather_db'),
    path('<int:pk>/weatherballdetails/', views.weather_details, name='weather_details'),
]
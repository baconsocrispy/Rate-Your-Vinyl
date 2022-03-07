from django.urls import path
from . import views



urlpatterns = [

    path('', views.Drones_home, name='Drones_home'),
    path('create/', views.Drones_create, name='Drones_create'),
]
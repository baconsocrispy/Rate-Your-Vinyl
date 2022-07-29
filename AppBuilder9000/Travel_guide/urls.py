from django.urls import path
from .import views

urlpatterns = [
    path('', views.travel_home, name='Travel_home'),
    path('create/', views.travel_create, name='Travel_create')
]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.Travel_home, name='Travel_home'),
    path('create/', views.Travel_create, name='Travel_create')
]

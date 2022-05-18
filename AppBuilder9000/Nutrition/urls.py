from django.urls import path
from . import views

urlpatterns = [
    path('', views.Nutrition_Home, name = 'Nutrition_Home'),
    path('Nutrition_create/', views.registerform, name = 'Nutrition_create')
]
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Recipes_Home, name="Recipes_Home"),
    path('Recipes_Create/', views.Recipes_Create, name="Recipes_Create"),
    path('Recipes_See/', views.Recipes_See, name="Recipes_See"),
]
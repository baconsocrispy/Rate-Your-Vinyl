from django.urls import path
from .import views

urlpatterns = [
    path('', views.Recipes_Home, name="Recipes_Home"),
]
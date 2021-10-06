from django.urls import path
from . import views

urlpatterns = [
    path('', views.Sushi_Recipes_Home, name="Sushi_Recipes_Home")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.sushi_recipes_home, name="Sushi_Recipes_Home")
]

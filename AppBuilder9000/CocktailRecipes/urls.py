from django.urls import path
from . import views

urlpatterns = [
    path('', views.cocktail_recipes_home, name='cocktail_recipes_home'),
]

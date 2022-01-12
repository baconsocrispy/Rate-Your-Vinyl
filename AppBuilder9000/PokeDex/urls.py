from django.urls import path
from .import views

urlpatterns = [
    path('', views.pokeDexHome, name='PokeDex_home'),
    path('addPokemon/', views.addPokemon, name='Add_Pokemon_to_PokeDex')
]
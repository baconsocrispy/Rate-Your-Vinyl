from django.urls import path
from .import views

urlpatterns = [
    path('', views.pokeDexHome, name='PokeDex_home'),
    path('addPokemon/', views.addPokemon, name='Add_Pokemon_to_PokeDex'),
    path('show_pokemon/', views.show_pokemon, name="show_pokemon"),
    path('<int:pk>/pokemonDetails/', views.pokemon_details, name="pokemon_details")
]
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PokemonForm
from .models import Pokemon

# imports needed to run BeautifulSoup and do web scraping
import requests
from bs4 import BeautifulSoup



# All of these functions here will need to be added to the urls.py files to be able to make them work and to call them

# this is just so we can go back to the home page when you click home on the navbar
def pokeDexHome(request):
    return render(request, 'PokeDex/PokeDex_home.html')

# here we are making it so that we are getting the info from the PokemonForm and saving the info to the database
# if the request.method == post and the form info is valid and then redirecting to the home page for now
def addPokemon(request):
    form = PokemonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('PokeDex_home')
    content = { 'form': form }
    return render(request, 'PokeDex/AddPokemon_form.html', content)

# this is how we are going to get the info from our models.py and then have that info returned and displayed onto
# hour showPokemon.html file
def show_pokemon(request):
    show_pokemon = Pokemon.object.all()

    context = {'show_pokemon': show_pokemon}
    return render(request, 'PokeDex/PokeDex_showPokemon.html', context)

# this is how we end up getting the primary key from our DB and use it to get and show the details when the pokemon name is selected
def pokemon_details(request, pk):
    details = get_object_or_404(Pokemon, pk=pk)
    context = {'details': details}
    return render(request, 'PokeDex/pokemonDetails.html', context)

def edit_pokemon(request, pk):
    show_pokemon = get_object_or_404(Pokemon, pk=pk)
    form = PokemonForm(data=request.POST or None, instance=show_pokemon)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_pokemon')
    context = {'form': form}
    return render(request, 'PokeDex/PokeDex_edit.html', context)

def delete_pokemon(request, pk):
    show_pokemon = get_object_or_404(Pokemon, pk=pk)
    form = PokemonForm(data=request.POST or None, instance=show_pokemon)
    if request.method == 'POST':
            show_pokemon.delete()
            return redirect('show_pokemon')
    return render(request, 'PokeDex/PokeDex_delete.html', {'show_pokemon': show_pokemon, 'form': form})

"""
======================================================
    BEAUTIFUL SOUP SECTION
========================================================================
"""

def pokeDex_search(request):
    pokemon = []
    page = requests.get("https://www.pokemon.com/us/pokedex/")
    soup = BeautifulSoup(page.content, 'html.parser')
    pokemon_info = soup.find_all('div', class_='pokemon-info')
    for i in pokemon_info:
        info = i.find_all('h5')
        info.get_text()
        pokemon.append(info)
    print(pokemon)
    return render(request, 'PokeDex/PokeDex_search.html')


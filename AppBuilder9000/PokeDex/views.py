from django.shortcuts import render, redirect, get_object_or_404
from .forms import PokemonForm
from .models import Pokemon
from django.contrib import messages

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

""" here we have our code to scrape the number and name of the pokemon from the pokemon.com website to put into our
search page later. We use the request.get here and put in the web link we are wanting to scrape the info from and then do
the beautifulSoup below and pass in the page content and have it sent back through html.parser and then we make 2 empty
lists that we will use further down to get the final info we want later. We then do a for loop to find all the 'li' tags
in the web link above and then wek ask to get the text from those and to strip them to a string and then we say if the 
length of the text is what we want to return the info and we append the info below and then we make a var to get the info
we want and pass in an example of what we want returned and then we do a while loop to get our final output and we get 
that by putting the name and number of the pokemon we get from our pokemon list into a var and then we append the var
and add 1 each time we run the while loop until we get to the final number and each time it runs it will get the pokemon
name and number assosiated with it and give it back to us and then we pass the final list into our context and have it
returned with our search.html page and then we will run the list in the search.html page to display the info we got from 
here."""
def pokeDex_search(request):
    page = requests.get("https://www.pokemon.com/us/pokedex/")
    soup = BeautifulSoup(page.content, 'html.parser')
    pokemon_list = []
    final_list = []
    for i in soup.find_all('li'):
        li_text = i.get_text(strip=True)
        if len(li_text):
            pokemon_list.append(li_text)
    d = pokemon_list.index('1 - Bulbasaur')
    i = 0
    while i < 898: # number of pokemon
        poke_list = pokemon_list[d + i]
        final_list.append(poke_list)
        i += 1
    context = {'final_list': final_list}
    return render(request, 'PokeDex/PokeDex_search.html', context)

"""
==================================================================================
    API SECTION 
=========================================================================================================
"""

def more_info(request):
    abilities = []
    species = []
    if request.method == "POST":
        value = request.POST['pokemon'].lower()
        if value == "":
            messages.info(request, 'Please enter in a Pokémon name!')
        else:
            info = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(value))
            poke_info = info.json()
            poke_name = poke_info
            poke_abilities = poke_name['abilities']
            first_ability = poke_abilities[0]
            second_ability = poke_abilities[1]
            poke_ability_one = first_ability['ability']
            poke_ability_two = second_ability['ability']
            ability_name_one = poke_ability_one['name']
            ability_name_two = poke_ability_two['name']
            abilities.append(ability_name_one)
            abilities.append(ability_name_two)
            poke_type = poke_name['types']
            first_type = poke_type[0]
            poke_type_one = first_type['type']
            type_name_one = poke_type_one['name']
            species.append(type_name_one)

        return render(request, 'PokeDex/PokeDex_api.html',
                      {'value': value,
                       'species': species,
                       'abilities': abilities})
    else:
        return render(request, 'PokeDex/PokeDex_api.html')





from django.shortcuts import render
from django.http import HttpResponse


def cocktail_recipes_home(request):
    return render(request, 'CocktailRecipes/cocktail_recipes_home.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Cocktail, Review
from .forms import CocktailForm, ReviewForm


# view function to render the cocktail recipes home page
def cocktail_recipes_home(request):
    # renders the homepage and passes active to the navbar
    return render(request, 'CocktailRecipes/cocktail_recipes_home.html', {'home_page': 'active'})


# view function to take user input and add new cocktail recipes to the database
def add_cocktail(request):
    form = CocktailForm(data=request.POST or None)
    # checks if the request method came from submitting the add cocktail form on this page
    # or from a link elsewhere in the app
    if request.method == 'POST':
        # validate the form against model parameters
        if form.is_valid():
            form.save()
            # this will eventually render the new cocktails page
            return cocktail_recipes_home(request)
    # if the request wasn't the POST method from the add cocktail form
    # render add_cocktail.html page, also create the dictionary content and
    # give it key value pair 'form': variable that contains CocktailForm, and
    # passes navbar active
    content = {'form': form, 'add_cocktail': 'active'}
    return render(request, 'CocktailRecipes/cocktail_recipes_add_cocktail.html', content)

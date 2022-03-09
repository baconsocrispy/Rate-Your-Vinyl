from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipes
from .forms import RecipesForm


def grandmas_recipes_home(request):
    return render(request, 'GrandmasRecipes/GrandmasRecipes_home.html')


def grandmas_recipes_library(request):
    grandmasrecipes_list = Recipes.GrandmasRecipes.all()
    context = {
        'Grandmasrecipes_list': grandmasrecipes_list
    }
    return render(request, 'GrandmasRecipes/GrandmasRecipes_Library.html', context)


def grandmas_recipes_addNew(request):
    form = RecipesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('GrandmasRecipes_home')
    context = {
        'form': form,
    }
    return render(request, 'GrandmasRecipes/GrandmasRecipes_AddNew.html', context)

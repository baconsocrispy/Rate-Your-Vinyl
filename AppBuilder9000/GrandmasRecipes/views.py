from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipesForm
from .models import Recipes


def grandmas_home(request):
    return render(request, 'GrandmasRecipes/GrandmasRecipes_home.html')


def grandmas_create(request):
    form = RecipesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('GrandmasRecipes_home')
    content = {'form': form}
    return render(request, 'GrandmasRecipes/GrandmasRecipes_create.html', content)


def grandmas_cookbook(request):
    # recipe = Database name: Recipes, model manager: Recipe get all
    recipes = Recipes.Recipes.all()
    context = {'recipes': recipes}

    return render(request, 'GrandmasRecipes/GrandmasRecipes_cookbook.html', context)

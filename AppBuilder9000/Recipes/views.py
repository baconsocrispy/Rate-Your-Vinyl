from django.shortcuts import render, redirect
from .forms import RecipesForm
from .models import Recipes


def recipes_home(request):
    return render(request, 'Recipes/recipeshome.html')


def recipes_create(request):
    form = RecipesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('recipes_home')
    context = {
        'form': form,
    }
    return render(request, 'Recipes/recipescreate.html', context)


def recipes_display(request):
    recipes_list = Recipes.Recipe.all()
    context = {
        'recipes_list': recipes_list
    }
    return render(request, 'Recipes/recipesdisplay.html', context)

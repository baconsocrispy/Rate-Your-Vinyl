from django.shortcuts import render, redirect, get_object_or_404
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


def recipes_details(request, pk):
    details = get_object_or_404(Recipes, pk=pk)
    context = {'details': details}
    return render(request, 'Recipes/recipesdetails.html', context)

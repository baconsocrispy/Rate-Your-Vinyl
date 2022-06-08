from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RecipeForm
from django.shortcuts import render, redirect, get_object_or_404


def veggie_home(request):
    return render(request, "Veggie_home.html")


def create_recipe(request):
    form = RecipeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
    context = {'form': form}
    return render(request, "Veggie/recipe_form.html", context)


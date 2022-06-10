from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RecipeForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe


# Create the home page
def veggie_home(request):
    return render(request, "Veggie_home.html")

# Adding a new recipe
def create_recipe(request):
    form = RecipeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../veggie_recipe')
    context = {'form': form}
    return render(request, "Veggie/veggie_form.html", context)

# Displays all the recipes one after the other
def display_veggie(request):
    all_recipe = Recipe.objects.all()
    return render(request, "Veggie/veggie_recipe.html", {'all_recipe': all_recipe})


# Display one recipe on a new page
def single_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'Veggie/veggie_details.html',  {'recipe': recipe})

# A Functioning edit page for any item in the database
def veggie_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=recipe)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../veggie_recipe')
    content = {'form': form, 'recipe': recipe}
    return render(request, 'Veggie/veggie_edit.html', content)


# Delete a recipe from the database
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('veggie_recipe')
    return render(request, 'Veggie/veggie_delete.html', {'recipe': recipe})




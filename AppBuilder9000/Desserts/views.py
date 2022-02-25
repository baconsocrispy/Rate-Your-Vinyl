from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe


# render home page
def home(request):
    return render(request, 'Desserts/desserts_home.html')


# render add_recipe page
def add_recipe(request):
    form = RecipeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('desserts_home')
    content = {'form': form}
    return render(request, 'Desserts/desserts_add_recipe.html', content)


# render display_Db page, display all recipes in database
def display_recipe_items(request):
    recipe_db = Recipe.Recipes.all()
    content = {'recipe_db': recipe_db}
    return render(request, 'Desserts/desserts_displayDb.html', content)


# render desserts_details page, display details of any single recipe in the database
def recipe_details(request, pk):
    details = get_object_or_404(Recipe, pk=int(pk))
    content = {'details': details}
    return render(request, 'Desserts/desserts_details.html', content)


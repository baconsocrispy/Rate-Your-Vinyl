from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredients, Instructions
from .forms import RecipeForm, IngredientsForm, InstructionsForm


# first instruction on what to do if "home" get invoked
def recipe_home(request):
    # renders in the browser
    return render(request, 'Recipe_Maker/Recipe_Maker_home.html')


def create_recipe(request):
    recipe_form = RecipeForm(request.POST or None)  # gets information from the form
    ingredients_form = IngredientsForm(request.POST or None)  # gets information from the form
    instructions_form = InstructionsForm(request.POST or None)  # gets information from the form
    # if all three forms are valid
    if recipe_form.is_valid() and ingredients_form.is_valid() and instructions_form.is_valid():
        # save information
        recipe_form.save()
        ingredients_form.save()
        instructions_form.save()
        # returns user "home"
        return redirect('recipe_home')
    # if not valid
    else:
        # prints errors
        print(recipe_form.errors)
        print(ingredients_form.errors)
        print(instructions_form.errors)
        # create an empty version of the forms and pass it into a dictionary
        recipe_form = RecipeForm()
        ingredients_form = IngredientsForm()
        instructions_form = InstructionsForm()
    context = {
        'recipe_form': recipe_form,
        'ingredients_form': ingredients_form,
        'instructions_form': instructions_form,
    }
    # returns the user to the create webpage with the dictionary
    return render(request, 'Recipe_Maker/Recipe_Maker_create.html', context)
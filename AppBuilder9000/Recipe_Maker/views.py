from django.shortcuts import render, get_object_or_404, redirect

from .forms import RecipeForm


# first instruction on what to do if "home" get invoked
def recipe_home(request):
    # renders in the browser
    return render(request, 'Recipe_Maker/Recipe_Maker_home.html')


def create_recipe(request):
    recipe_form = RecipeForm(request.POST or None)  # gets information from the form

    # if the form is valid
    if recipe_form.is_valid():
        # save information
        recipe_form.save()
        # returns user "home"
        return redirect('Recipe_Maker')
    # if not valid
    else:
        # prints errors
        print(recipe_form.errors)
        # create an empty version of the forms and pass it into a dictionary
        recipe_form = RecipeForm()
    context = {
        'recipe_form': recipe_form,
    }
    # returns the user to the create webpage with the dictionary
    return render(request, 'Recipe_Maker/Recipe_Maker_create.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe
# import pagination
from django.core.paginator import Paginator


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


def list_recipes(request):
    recipe_list = Recipe.objects.all()
    '''
    # set up Pagination
    p = Paginator(Recipe.objects.all(), 2)
    page = request.GET.get('page')
    recipes = p.get_page(page)
    '''
    return render(request, 'Recipe_Maker/Recipe_Maker_display.html', {'recipe_list': recipe_list})

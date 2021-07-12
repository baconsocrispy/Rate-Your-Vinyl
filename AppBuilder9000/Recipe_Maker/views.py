from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe
# import pagination
from django.core.paginator import Paginator


# first instruction on what to do if "home" get invoked
def recipe_home(request):
    # renders in the browser
    return render(request, 'Recipe_Maker/Recipe_Maker_home.html')

# creates a new entry in the database
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

# lists out items in the database
def list_recipes(request):
    # old code to display items in database
    # recipe_list = Recipe.objects.all()

    # set up Pagination
    p = Paginator(Recipe.objects.all(), 2)
    page = request.GET.get('page')
    recipes = p.get_page(page)

    return render(request, 'Recipe_Maker/Recipe_Maker_display.html', {'recipes': recipes})


# function to display a detailed view of items
def details(request, pk):
    # info from a url is in a string so it needs to be converted to integer
    pk = int(pk)
    item = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect(form.errors)
        else:
            print(form.errors)
    else:
        return render(request, 'Recipe_Maker/Recipe_Maker_details.html', {'form': form}))

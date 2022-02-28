from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe
from bs4 import BeautifulSoup
import requests


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


# render desserts_edit page, save modifications back to database
def edit_recipe(request, pk):
    item = get_object_or_404(Recipe, pk=int(pk))  # the recipe we want to modify
    form = RecipeForm(data=request.POST or None, instance=item)  # create form instance and bind data to it

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('desserts_displayDb')  # return to database list
        else:
            print(form.errors)
    content = {'form': form}
    return render(request, 'Desserts/desserts_edit.html', content)


# render desserts_delete page, save to database
def delete_recipe(request, pk):
    item = get_object_or_404(Recipe, pk=int(pk))  # the recipe we want to delete
    form = RecipeForm(data=request.POST or None, instance=item) # create form instance and bind data to it
    if request.method == 'POST':
        item.delete()
        return redirect('desserts_displayDb')  # return to database list
    content = {
        'item': item,
        'form': form,
    }
    return render(request, 'Desserts/desserts_delete.html', content)


def scrape_desserts(request):
    names = []  # recipe name list
    descriptions = []  # recipe description list
    url = 'https://www.spoonforkbacon.com/category/dessert-recipes/'  # page to scrape data from
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    dessert_soup = soup.find('article', class_="category-dessert-recipes")
    dessert_name = dessert_soup.find_all('h2', class_="entry-title")  # get dessert name
    dessert_description = dessert_soup.find_all('div', class_="entry-content")  # get dessert description

    for i in dessert_name:
        name = i.text
        names.append(name)

    for j in dessert_description:
        description = j.text
        descriptions.append(description)

    zipped_list = zip(names, descriptions)
    context = {'zipped_list': zipped_list}

    return render(request, 'Desserts/desserts_bs.html', context)
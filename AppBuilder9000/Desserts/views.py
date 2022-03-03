import re

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe
from bs4 import BeautifulSoup
import requests
import json


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


# scrape recipe data from external recipe page, package up and send to template to be rendered
def scrape_desserts(request):
    names = []  # recipe name list
    descriptions = []  # recipe description list
    recipe_urls = []  # recipe_url list
    url = 'https://www.spoonforkbacon.com/category/dessert-recipes/'  # page to scrape data from
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    parental_soup = soup.find_all('article', class_="category-dessert-recipes")  # parent to search

    for i in parental_soup:  # iterate through parental_soup through each article tag
        name = i.h2.a.text  # extract text from h2 hyperlink text as recipe name
        description = i.div.p.text  # extract text from first paragraph tag in the div inside parental soup
        recipe_url = i.find('a')['href']  # extract recipe urls
        names.append(name)  # append name to names list
        descriptions.append(description)  # append description to descriptions list
        recipe_urls.append(recipe_url)  # append recipe urls to recipe_urls list

    zipped_list = zip(names, descriptions, recipe_urls) # zip all extracted lists together
    context = {'zipped_list': zipped_list} # bind zipped_list dictionary to context

    print(names)  # output to console
    print(descriptions)  # output to console
    print(recipe_urls) # output to console
    return render(request, 'Desserts/desserts_bs.html', context)


# recipe_search function returns all recipes found at the source site
#   API Source: https://rapidapi.com/masterfahim-8ILF-zz7IG3/api/cooking-recipe2/
def recipe_search(request):
    url = "https://cooking-recipe2.p.rapidapi.com/"  # api source url

    headers = {  # required headers
        'x-rapidapi-host': "cooking-recipe2.p.rapidapi.com",
        'x-rapidapi-key': "08bef4aa77msh6b7038e100877f0p112618jsn4fa53277c30a"
    }

    response = requests.request("GET", url, headers=headers)  # get the data
    recipe_parsed = json.loads(response.text)  # parse the data

    for recipe in recipe_parsed:  # iterate through parsed data, pull out the pieces we want
        results = {
            'name': recipe['title'], # get recipe name
            'category': recipe['category'],  # get recipe category
            'recipe_url': recipe['url']  # get source url
        }
        print(results)  # print retrieved data pieces to console

    # print(response.text)  # all available data
    return render(request, 'Desserts/desserts_search.html')


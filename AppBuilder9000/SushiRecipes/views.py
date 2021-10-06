from django.shortcuts import render



def sushi_recipes_home(request):
    return render(request, 'SushiRecipes/Sushi_Recipes_Home.html')

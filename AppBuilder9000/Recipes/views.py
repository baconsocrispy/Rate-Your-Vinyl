from django.shortcuts import render


def recipes_home(request):
    return render(request, 'Recipes/recipeshome.html')

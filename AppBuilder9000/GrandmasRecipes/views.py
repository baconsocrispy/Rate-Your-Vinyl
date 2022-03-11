from django.shortcuts import render, get_object_or_404, redirect


def grandmas_home(request):
    return render(request, 'GrandmasRecipes/GrandmasRecipes_home.html')




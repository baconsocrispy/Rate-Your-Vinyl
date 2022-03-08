from django.shortcuts import render, get_object_or_404, redirect


def grandmasrecipes_home(request):
    # render method takes the request object and template name as arguments
    # returns httpResponse object with rendered text.
    return render(request, 'GrandmasRecipes_base.html')

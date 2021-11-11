from django.shortcuts import render, redirect


def hotsprings_home(request):
    # render method takes the request object and template name as arguments
    # returns httpResponse object with rendered text.
    return render(request, 'hotsprings_home.html')

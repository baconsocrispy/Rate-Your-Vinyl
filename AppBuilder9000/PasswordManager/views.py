from django.shortcuts import render


def home(request): # renders the 'home page' @ templates/home.html
    return render(request, 'home.html')

# Create your views here.

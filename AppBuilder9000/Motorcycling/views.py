from django.shortcuts import render
import requests


# Create your views here.

# This creates the function that leads the user to the home page.
def motorcycling_home(request):
    return render(request, 'Motorcycling/motorcycling_home.html')

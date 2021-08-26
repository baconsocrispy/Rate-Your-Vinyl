from django.shortcuts import render
from .forms import PlayerForm


# Displays Home Page
def BlazerStats_Home(request):
    return render(request, 'BlazerStats/home.html')



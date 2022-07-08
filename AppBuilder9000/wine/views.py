from django.shortcuts import render, get_object_or_404, redirect
from .forms import WinesForm
from .models import Wines
from django.http import HttpResponse
import requests

# Story#1: Create the app
# Render the home page
def wine_home(request):
    return render(request, "wine/wine_home.html")

def wine_type(request):
    return render(request, "wine/wine_type.html")


# Story #2: Create your model
def wine_create(request):
    form = WinesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, "wine/wine_create.html", content)

# Story #3: Display all items from database
def wine_pair(request):
    entry = Wines.objects.all()
    content = {'entry': entry}
    return render(request, 'wine/wine_pair.html', content)



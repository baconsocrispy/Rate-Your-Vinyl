from django.shortcuts import render, redirect
from .forms import CharacterForm, SeriesForm
import requests

# Create your views here.
def home(request):
    return render(request, 'FictionalCharacters/FictionalCharacters_Home.html')

# Create a function
def series_create(request):
    form = SeriesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('FictionalCharacters_CreateSeries')
        else:
            print(form.errors)
            form = SeriesForm()
    context = {'form': form}
    return render(request,  'FictionalCharacters/FictionalCharacters_CreateSeries.html', context)

# Create a function
def characters_create(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('FictionalCharacters_Create')
        else:
            print(form.errors)
            form = CharacterForm()
    context = {'form': form}
    return render(request, 'FictionalCharacters/FictionalCharacters_Create.html', context)
from django.shortcuts import render, redirect
from .forms import CharacterForm, SeriesForm
from .models import Characters
import requests

# Create your views here.
def home(request):
    return render(request,
    'FictionalCharacters/FictionalCharacters_Home.html')

# Create a function to add a series to dB
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
    return render(request,
    'FictionalCharacters/FictionalCharacters_CreateSeries.html', context)

# Create a function to add a character to dB
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
    return render(request,
    'FictionalCharacters/FictionalCharacters_Create.html', context)

# Create a function to list entries in Characters dB
def list_characters(request):
    # Retrieves all entries from dB in alphabetical order by name
    char_sort = Characters.objects.order_by('name')
    return render(request,
    'FictionalCharacters/FictionalCharacters_View.html', {'chars': char_sort})

# Create a function to list search results of Characters dB
def search_characters(request):
    if request.method == "POST":
        searched = request.POST['searched']
        chars = Characters.objects.filter(name__contains=searched)
        return render(request,
        'FictionalCharacters/FictionalCharacters_Search.html', {'searched': searched, 'chars': chars})
    else:
        return render(request,
        'FictionalCharacters/FictionalCharacters_Search.html', {})


def show_char(request, char_id):
    char = Characters.objects.get(pk=char_id)
    return render(request,
    'FictionalCharacters/FictionalCharacters_ShowChar.html', {'char': char})
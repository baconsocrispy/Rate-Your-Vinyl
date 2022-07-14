import json

from django.conf.locale import gl
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm
from .models import Character
import requests
import json


# Create your views here.

# Story #1: Build the basic app

def marvel_home(request):
    return render(request, "Marvel/marvel_home.html", )


# Story #2: Create your model

def marvel_create(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marvel_roster')
    content = {'form': form}
    return render(request, 'Marvel/marvel_create.html', content)


# Story #3: Display all items from the database

def marvel_roster(request):
    character = Character.Characters.all()
    content = {'character': character}
    return render(request, 'Marvel/marvel_roster.html', content)


# Story #4: Details page

def marvel_details(request, pk):
    character = get_object_or_404(Character, pk=pk)
    content = {'character': character}
    return render(request, 'Marvel/marvel_details.html', content)


# Story #5: Edit and Delete Functions

def marvel_update(request, pk):
    character = get_object_or_404(Character, pk=pk)
    form = CharacterForm(data=request.POST or None, instance=character)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marvel_roster')
    content = {'form': form, 'character': character}
    return render(request, 'Marvel/marvel_update.html', content)


def marvel_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        character.delete()
        return redirect('marvel_roster')
    content = {'character': character}
    return render(request, 'Marvel/marvel_delete.html', content)


# Story 6/7: API

def marvel_api(request):
    url = "https://marvel-quote-api.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Host": "marvel-quote-api.p.rapidapi.com",
        "X-RapidAPI-Key": "bca2057807mshfe7effe0d91b0fap1b9154jsnceb9849a546b"
    }

    response = requests.request("GET", url, headers=headers, )

    api_info = json.loads(response.text)
    quote = api_info["Quote"]
    speaker = api_info["Speaker"]
    content = {"quote": quote, "speaker": speaker}
    return render(request, 'marvel/marvel_api.html', content)

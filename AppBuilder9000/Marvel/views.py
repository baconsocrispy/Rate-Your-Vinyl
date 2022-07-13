from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm
from .models import Character


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

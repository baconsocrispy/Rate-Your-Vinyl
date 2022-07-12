from django.shortcuts import render, redirect
from .forms import CharacterForm


# Create your views here.

# Story #1: Build the basic app

def marvel_home(request):
    return render(request, "Marvel/marvel_home.html",)


# Story #2: Create your model

def marvel_create(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marvel_home')
    content = {'form': form}
    return render(request, 'Marvel/marvel_create.html', content)

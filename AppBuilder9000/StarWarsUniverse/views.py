from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from . forms import CharacterForm
from .models import Character


def home(request):
    return render(request, 'swu_home.html')


def sources(request):
    return render(request, 'swu_sources.html')


def characters(request):
    form = CharacterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("swu_characters")
    return render(request, 'swu_characters.html', {'form': form})




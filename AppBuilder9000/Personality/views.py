from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, ComparedPerson
from .forms import PersonForm


def personality_home(request):
    return render(request, 'Personality/personality_home.html')


def personality_create(request):
    return render(request, 'Personality/personality_create.html')


def personality_compare(request):
    return render(request, 'Personality/personality_compare.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Traveler, Place
from .forms import TravelerForm, PlaceForm


def Traveling_home(request):
    return render(request, 'Traveling/Traveling_home.html')
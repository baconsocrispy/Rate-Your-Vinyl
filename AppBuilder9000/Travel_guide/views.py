from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm
import requests


def travel_home(request):
    return render(request, 'Travel_home.html')


def travel_create(request):
    form = DestinationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'Travel_create.html', content)

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Location
from .forms import LocationForm
from .forms import User




def TrackApp_home(request):
    return render(request,"TrackApp\TrackApp_home.html")

def TrackApp_Add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TrackApp_Add')
    else:
        form = LocationForm(request.POST)
        return render(request, 'TrackApp/TrackApp_Add.html',
                      {'form': form})

def TrackApp_create(request):
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TrackApp_create')
    else:
        form = createForm(request.POST)
        return render(request, 'TrackApp/TrackApp_create.html')






















from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Location
from .forms import LocationForm
from .forms import User
from .forms import DisplayForm





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
def TrackApp_display(request):
    if request.method == 'POST':
        form = DisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TrackApp_display')
    else:
        form = DisplayForm(request.POST)
        return render(request, 'TrackApp/TrackApp_display',
                      {'form': form})





























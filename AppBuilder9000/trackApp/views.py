from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocationForm
from django.db import models
from .forms import LocationForm










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
    detail = LocationForm.objects.all()
    context = {'detail': detail}
    return render(request, "TrackApp/TrackApp_display.html", context)

def TrackApp_detail(request, pk):
    location_name = get_object_or_404(Review, pk=pk)
    all_detail = {'TrackApp_detail': TrackApp_detail}
    context = all_detail
    return render(request, "TrackApp/TrackApp_detail", context)




































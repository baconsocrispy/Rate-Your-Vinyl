from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import TrackForm
from .models import TrackApp



def TrackApp_home(request):
    return render(request,"TrackApp\TrackApp_home.html")

def TrackApp_Add(request):
    if request.method == 'POST':
        form = TrackAppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TrackApp_Add')
    else:
        form = TrackAppForm(request.POST)
        return render(request, 'TrackApp/TrackApp_Add.html',
                      {'form': form})

















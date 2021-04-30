from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import TrackApp
from .models import CHOICES
from .forms import TrackApp



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
def home_view(request):
    context ={}
    form = TrackApp(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "TrackApp_home.html", context)



















from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm
import requests


def travel_home(request):
    return render(request, 'Travel_home.html')


def travel_create(request):
    form = DestinationForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Travelguide_base.html')
    else:
        print(form.errors)
        form = DestinationForm()
    context = {
        'form': form,
    }
    return render(request, "Travel_create.html", context)


def travel_read(request):
    d = Destination.objects.all()
    return render(request, 'Travel_read.html', {'Destination': d})

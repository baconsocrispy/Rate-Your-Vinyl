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
        return redirect('Travel_read')
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


def travel_details(request, pk):
    entry = get_object_or_404(Destination, pk=pk)
    content = {'entry': entry}
    return render(request, 'Travel_details.html', content)


def travel_edit(request, pk):
    entry = get_object_or_404(Destination, pk=pk)
    form = DestinationForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Travel_details')
    content = {'form': form, 'entry': entry}
    return render(request, 'Travel_edit.html', content)


def travel_delete(request, pk):
    entry = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('Travel_details')
    content = {'entry': entry}
    return render(request, 'Travel_delete.html', content)
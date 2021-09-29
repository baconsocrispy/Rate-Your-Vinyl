from django.shortcuts import render, get_object_or_404, redirect
from .eurotripforms import AccommodationsForm, thingsToDoForm, LocationForm
# pulls in the data from all EuroTrip classes
from .models import Accommodations, thingsToDo, Location


def eurotriphome (request):
    return render(request, 'eurotriphome.html')


def eurotrip_accomodations (request):
    return render (request, 'eurotrip_accomodations.html')


def eurotrip_locations (request):
    return render(request, 'eurotrip_locations')


def thingtodo (request):
    return render(request, 'eurotrip_thingtodo')


def eurotrip_accomcreate(request):
    form = AccommodationsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eurotrip_accomodations')
    else:
        print(form.errors)
        form = AccommodationsForm()
        context = {
            'form': form,
        }
    return render(request, 'eurotrip_accomcreate.html', context)


def eurotrip_ttdcreate(request):
    form = thingsToDoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eurotrip_thingtodo')
    else:
        print(form.errors)
        form = thingsToDoForm()
        context = {
            'form': form,
        }
    return render(request, 'eurotrip_ttdcreate.html', context)


def eurotrip_loccreate(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eurotrip_locations')
    else:
        print(form.errors)
        form = LocationForm()
        context = {
            'form': form,
        }
    return render(request, 'eurotrip_loccreate.html', context)



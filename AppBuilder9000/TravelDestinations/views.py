from django.shortcuts import render, redirect, get_object_or_404
from .forms import DestinationForm
from .models import destination


def home(request):
    return render(request, 'TravelDestinations/TravelDestinations_home.html')


def TravelDestinations_add(request):
    form = DestinationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('TravelDestinations_add.html')
    content = {'form': form}
    return render(request, 'TravelDestinations/TravelDestinations_add.html', content)


def destinations(request):
    trips = destination.destination.all()
    content = {'trips': trips}
    return render(request, 'TravelDestinations/TravelDestinations_destinations.html', content)


def trip_details(request, id):
    details = destination.destination.get(id=id)
    content = {'details': details}
    return render(request, 'TravelDestinations/TravelDestinations_details.html', content)

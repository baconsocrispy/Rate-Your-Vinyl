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


def trip_edit(request, id):
    item_details = get_object_or_404(destination, id=id)
    form = DestinationForm(request.POST or None, instance=item_details)
    if form.is_valid():
        form.save()
        return redirect('TravelDestinations_destinations.html')
    content = {'form': form}
    return render(request, 'TravelDestinations/TravelDestinations_edit.html', content)


def trip_delete(request, id):
    data = get_object_or_404(destination, id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('TravelDestinations_destinations.html')
    delete = {'data': data}
    return render(request, 'TravelDestinations/TravelDestinations_delete.html', delete)

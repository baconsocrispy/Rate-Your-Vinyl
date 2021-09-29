from django.shortcuts import render, get_object_or_404, redirect
from .eurotripforms import AccommodationsForm, thingsToDoForm, LocationForm, PricingForm
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


def prices (request):
    return render(request, 'eurotrip_prices')


def eurotrip_accomcreate(request):
    form1 = AccommodationsForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        return redirect('eurotrip_accomodations')
    else:
        print(form1.errors)
        form1 = AccommodationsForm()
        context = {
            'form': form1,
        }
    return render(request, 'eurotrip_accomcreate.html', context)


def eurotrip_ttdcreate(request):
    form2 = thingsToDoForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        return redirect('eurotrip_thingtodo')
    else:
        print(form2.errors)
        form2 = thingsToDoForm()
        context = {
            'form': form2,
        }
    return render(request, 'eurotrip_ttdcreate.html', context)


def eurotrip_loccreate(request):
    form3 = LocationForm(request.POST or None)
    if form3.is_valid():
        form3.save()
        return redirect('eurotrip_locations')
    else:
        print(form3.errors)
        form3 = LocationForm()
        context = {
            'form': form3,
        }
    return render(request, 'eurotrip_loccreate.html', context)


def eurotrip_pricecreate(request):
    form = PricingForm(request.POST or None)
    if form4.is_valid():
        form4.save()
        return redirect('eurotrip_prices')
    else:
        print(form4.errors)
        form4 = AccommodationsForm()
        context = {
            'form': form4,
        }
    return render(request, 'eurotrip_pricecreate.html', context)



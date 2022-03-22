from django.shortcuts import render, redirect, get_object_or_404
from .models import Traveler, Place
from .forms import TravelerForm, PlaceForm


def Traveling_home(request):
    return render(request, 'Traveling/Traveling_home.html')

def Traveling_create(request):
    form = TravelerForm(data=request.POST or None)
    #if method = post get data
    if request.method == 'POST':
        if form.is_valid():
            #check if it is valid
            form.save()
            return redirect('Traveling_home')
    context = {'form':form}
    return render(request, 'Traveling/Traveling_create.html', context)



def Traveling_place(request):
    travelers = Traveler.travelers.all()
    places = Place.places.all()
    return render(request, 'Traveling/Traveling_place.html', {'places': places, 'travelers': travelers})




















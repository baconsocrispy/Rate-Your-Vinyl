from django.shortcuts import render, redirect
from .models import SportsCar
from .forms import SportsCarForm


def SportsCars_Home(request):
    return render(request, 'SportsCars_Home.html')


def AddNewCar(request):
    form = SportsCarForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SportsCars_Home')
    content = {'form': form}
    return render(request, 'AddSportsCar.html', content)

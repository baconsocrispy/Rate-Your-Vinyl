from django.shortcuts import render, redirect, get_object_or_404
from .models import Motorcycle
from .forms import MotorcycleForm, RouteForm
import requests


# Create your views here.
def admin_console(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, 'products/products_page.html', {'motorcycles': Motorcycle})


# This creates the function that leads the user to the home page.
def motorcycling_home(request):
    return render(request, 'Motorcycling/motorcycling_home.html')


def create_motorcycle(request):
    form = MotorcycleForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('rate_motorcycle')
        else:
            print(form.errors)
            form = MotorcycleForm()
    context = {'form': form}
    return render(request, 'Motorcycling/rate_motorcycle.html', context)



def create_route(request):
    form = RouteForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('rate_route')
        else:
            print(form.errors)
            form = RouteForm()
    context = {'form': form}
    return render(request, 'Motorcycling/rate_route.html', context)


def motorcycle_list(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, 'Motorcycling/create_motorcycle_record.html', {'motorcycles': motorcycles})
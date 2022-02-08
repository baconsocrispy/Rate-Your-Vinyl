from django.shortcuts import render, redirect, get_object_or_404
from .models import Motorcycle, Route
from .forms import MotorcycleForm, RouteForm
from django.http import HttpResponseRedirect
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


def all_motorcycles(request):
    motorcycle_list = Motorcycle.objects.all()
    return render(request, 'Motorcycling/list_motorcycles.html', {'motorcycle_list': motorcycle_list})


# This allows the user to delete an item in the database
def motorcycle_delete(request, pk):
    item = get_object_or_404(Motorcycle, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list_motorcycles.html')
    context = {'Motorcycle': Motorcycle}
    return render(request, 'Motorcycling/list_motorcycles.html', context)


def all_routes(request):
    route_list = Route.objects.all()
    return render(request, 'Motorcycling/list_routes.html', {'route_list': route_list})


# This function will query the database and return a result per the user's request.
def motorcycle_details(request, pk):
    motorcycle_detail = get_object_or_404(Motorcycle, pk=pk)
    return render(request, 'Motorcycling/motorcycle_details.html', {'motorcycle_detail': motorcycle_detail})


def route_details(request, pk):
    route_detail = get_object_or_404(Route, pk=pk)
    return render(request, 'Motorcycling/route_details.html', {'route_detail': route_detail})
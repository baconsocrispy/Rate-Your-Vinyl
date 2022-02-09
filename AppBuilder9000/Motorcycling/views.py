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
def delete_motorcycle_admin(request, pk):
    item = get_object_or_404(Motorcycle, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list_motorcycles.html')
    context = {'Motorcycle': Motorcycle}
    return render(request, 'Motorcycling/list_motorcycles.html', context)

# This function will list all the saved routes
def all_routes(request):
    route_list = Route.objects.all()
    return render(request, 'Motorcycling/list_routes.html', {'route_list': route_list})


# This function will query the database and return a result per the user's request.
def motorcycle_details(request, pk):
    motorcycle_detail = get_object_or_404(Motorcycle, pk=pk)
    return render(request, 'Motorcycling/motorcycle_details.html', {'motorcycle_detail': motorcycle_detail})


# This function shows specific route data to the user
def route_details(request, pk):
    route_detail = get_object_or_404(Route, pk=pk)
    return render(request, 'Motorcycling/route_details.html', {'route_detail': route_detail})


# This function will let a user edit their data on the motorcycle
def update_motorcycle(request, pk):
    edit_motorcycle = get_object_or_404(Motorcycle, pk=pk)
    form = MotorcycleForm(data=request.POST or None, instance=edit_motorcycle)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_motorcycles')
    return render(request, 'Motorcycling/update_motorcycle.html', {'edit_motorcycle': edit_motorcycle, 'form': form})


# This function allows the user to delete the item in the database
def delete_motorcycle(request, pk):
    delete_user_motorcycle = get_object_or_404(Motorcycle, pk=pk)
    form = MotorcycleForm(data=request.POST or None, instance=delete_user_motorcycle)
    if request.method == 'POST':
        delete_user_motorcycle.delete()
        return redirect('list_motorcycles')
    return render(request, 'Motorcycling/delete_motorcycle.html',
                  {'delete_user_motorcycle': delete_user_motorcycle, 'form': form})


# This will allow the user to make updates to the database
def update_route(request, pk):
    route = get_object_or_404(Route, pk=pk)
    form = RouteForm(data=request.POST or None, instance=route)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_routes')
    return render(request, 'Motorcycling/update_route.html', {'route': route, 'form': form})


# This will allow the user to make updates to the database
def delete_route(request, pk):
    delete_user_route = get_object_or_404(Route, pk=pk)
    form = RouteForm(data=request.POST or None, instance=delete_user_route)
    if request.method == 'POST':
        delete_user_route.delete()
        return redirect('list_routes')
    return render(request, 'Motorcycling/delete_route.html', {'delete_user_route': delete_user_route, 'form': form})

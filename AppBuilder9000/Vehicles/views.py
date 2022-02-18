
from django.shortcuts import render, redirect

def vehiclesHome(request):
    return render(request, 'vehicles/Vehicles_home.html')

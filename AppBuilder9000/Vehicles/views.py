from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehiclesForm
from .models import Vehicles



def vehiclesHome(request):
    return render(request, 'vehicles/Vehicles_home.html')

def addVehicles(request):
    form = VehiclesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vehiclesHome')
    content = { 'form': form }
    return render(request, 'vehicles/Vehicles_add.html', content)



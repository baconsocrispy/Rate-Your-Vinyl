from django.http import HttpResponseRedirect
from django.shortcuts import render,  redirect, get_object_or_404
from .forms import DroneForm
from .models import Drone
# Create your views here.


def Drones_home(request):
    return render(request, 'Drones/Drones_home.html', {})


def Drones_create(request):
    form = DroneForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Drones_list')
    context = {'form': form}
    return render(request, 'Drones/Drones_create.html', context)


def Drones_list(request):
    drones_list = Drone.Drones.all()
    print('drones_list')
    return render(request, 'Drones/Drones_list.html', {'drones_list': drones_list })


def Drones_details(request):
    drone_details = get_object_or_404(Drone.Drones)
    context = {'drone_details': drone_details}
    return render(request, 'Drones/Drones_details.html', context)

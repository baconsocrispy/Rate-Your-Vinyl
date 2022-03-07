from django.shortcuts import render,  redirect, get_object_or_404
from .models import Drone
from .forms import DroneForm
import requests
# Create your views here.




def Drones_home(request):
    return render(request, 'Drones/Drones_home.html', {})

def Drones_create(request):
    form = DroneForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Drones_create.html')
    context = {'form': form}
    return render(request, 'Drones/Drones_create.html', context)




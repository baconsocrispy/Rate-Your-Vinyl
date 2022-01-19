from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import Airplaneform
from .models import Airplane



def homepage(request):
    return render(request, 'ComercialAirplanes/ComercialAirplane_home.html')

def addpage(request):
    form = Airplaneform(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ComercialAirplanes_home')
    else:
        print(form.errors)
        form = Airplaneform()
    context = {
        'form': form,
    }
    return render(request, 'ComercialAirplanes/ComercialAirplanes_add.html', context)

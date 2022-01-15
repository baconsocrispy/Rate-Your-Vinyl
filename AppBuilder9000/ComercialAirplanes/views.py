from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Airplane
from .forms import Airplaneform


def homepage(request):
    return render(request, 'ComercialAirplanes/ComercialAirplane_home.html')

def addpage(request):
    form = Airplaneform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ComercialAirplanes/ComercialAirplane_home.html')
    else:
        print(form.errors)
        form = Airplaneform()
    context = {
        'form': form,
    }
    return render(request, 'ComercialAirplanes/ComercialAirplane_add.html', context)


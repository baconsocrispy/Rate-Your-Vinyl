from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'ComercialAirplanes/ComercialAirplanes_home.html')


from django.shortcuts import render
from .models import House


def housing_costs_home(request):
    return render(request, "HousingCosts/HousingCosts_home.html")

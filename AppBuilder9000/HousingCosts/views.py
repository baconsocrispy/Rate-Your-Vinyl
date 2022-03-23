from django.shortcuts import render

def housing_costs_home(request):
    return render(request, "HousingCosts/HousingCosts_home.html")

from django.shortcuts import render, redirect
from .models import House
from .forms import HouseForm


def housing_costs_home(request):
    return render(request, "HousingCosts/HousingCosts_home.html")

# Contains the modelForm
def housing_costs_create(request):
    form = HouseForm()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            # This resets the form contents so it is empty after clicking 'submit':
            form = HouseForm()
    # This points to our HouseForm modelForm:
    context = {'form': form}
    return render(request, "HousingCosts/HousingCosts_create.html", context)

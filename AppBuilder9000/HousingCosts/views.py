from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from .models import House
from .forms import HouseForm
import requests
import json


def housing_costs_home(request):
    return render(request, "HousingCosts/HousingCosts_home.html")


# Contains the modelForm
def housing_costs_create(request):
    form = HouseForm()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            # This resets the form contents, so it is empty after clicking 'submit':
            form = HouseForm()
    # This points to our HouseForm modelForm (defined above):
    context = {'form': form}
    return render(request, "HousingCosts/HousingCosts_create_update.html", context)


def housing_costs_list(request):
    house_list = House.Homes.all()
    context = {'house_list': house_list}
    return render(request, 'HousingCosts/HousingCosts_list.html', context)


# This view creates the Details page based on the primary key of the DB item that is clicked.
def housing_costs_details(request, pk):
    pk = int(pk)
    details = get_object_or_404(House, pk=pk)
    context = {'details': details}
    return render(request, 'HousingCosts/HousingCosts_details.html', context)


# This view uses the same template as the create view, and pre-populates the form with
# the selected house's details. The submit button updates the info stored in DB.
def housing_costs_edit(request, pk):
    house = get_object_or_404(House, pk=pk)
    form = HouseForm(instance=house)

    if request.method == 'POST':
        # this is necessary so that we update existing record, rather than create a new one:
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            # If the form is saved, redirect to the details pg for this house.
            return redirect(housing_costs_details, pk=pk)

    context = {'form': form}
    return render(request, 'HousingCosts/HousingCosts_create_update.html', context)


def housing_costs_delete(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        house.delete()
        return redirect(housing_costs_list)
    context = {'details': house}
    return render(request, 'HousingCosts/HousingCosts_delete.html', context)


def realty_api_display(request):
    # API endpoint, headers, and required parameters. Python generates request url automagically from these:
    url = 'https://realty-in-us.p.rapidapi.com/properties/list-for-sale'
    headers = {
        'X-RapidAPI-Host': 'realty-in-us.p.rapidapi.com',
        'X-RapidAPI-Key': '1dda6feeefmsh95fcaa253de27e3p137c53jsn9f798d0c5753'
    }
    # limited to 10 Houses:
    payload = {
        'state_code': 'ME',
        'city': 'Portland',
        'offset': '0',
        'limit': '10',
        'sort': 'relevance'
    }
    # response contains extra data. I only want listings dictionary items:
    # 'address', 'beds', 'bath', 'sqft', 'price'
    response = requests.get(url, headers=headers, params=payload).json()
    # This grabs only ['listings'] data so I can use it in template. Not formatted:
    listings = response['listings']
    # print the entire response to the terminal:
    print(response)
    return render(request, 'HousingCosts/HousingCosts_api.html', {'listings': listings})

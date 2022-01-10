from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from .forms import PetForm
import requests
import json
from bs4 import BeautifulSoup


def pet_adoption_home(request):
    return render(request, 'PetAdoption/PetAdoption_home.html')


def pet_adoption_list(request):
    form = PetForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pet_adoption_home')
    context = {'form': form}
    return render(request, 'PetAdoption/PetAdoption_list.html', context)


def pet_adoption_dogs(request):
    dogs = Pet.Pets.all().filter(species='Dog')
    context = {'dogs': dogs}
    return render(request, 'PetAdoption/PetAdoption_dogs.html', context)


def pet_adoption_cats(request):
    cats = Pet.Pets.all().filter(species='Cat')
    context = {'cats': cats}
    return render(request, 'PetAdoption/PetAdoption_cats.html', context)


def pet_adoption_other(request):
    others = Pet.Pets.all().filter(species='Other')
    context = {'others': others}
    return render(request, 'PetAdoption/PetAdoption_other.html', context)


def pet_adoption_all(request):
    pets = Pet.Pets.all()
    context = {'pets': pets}
    return render(request, 'PetAdoption/PetAdoption_all.html', context)


def pet_adoption_details(request, pk):
    details = get_object_or_404(Pet, pk=pk)
    context = {'details': details}
    return render(request, 'PetAdoption/PetAdoption_details.html', context)


def pet_adoption_edit(request, pk):
    details = get_object_or_404(Pet, pk=pk)
    form = PetForm(data=request.POST or None, instance=details)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pet_adoption_all')
    context = {'details': details, 'form': form}
    return render(request, 'PetAdoption/PetAdoption_edit.html', context)


def pet_adoption_delete(request, pk):
    item = get_object_or_404(Pet, pk=pk)
    form = PetForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('pet_adoption_all')
    context = {'item': item, 'form': form}
    return render(request, 'PetAdoption/PetAdoption_deleteconfirm.html', context)


# Use BeautifulSoup to scrape adoption data
def pet_adoption_statistics(request):
    pet_list = []
    page = requests.get("https://humanepro.org/page/pets-by-the-numbers")
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the correct table (Shelter & Rescue group Estimates at bottom of page
    table = soup.find_all('table')[4]
    # choose the rows we want (just cats & Dogs)
    rows = table.find_all('tr')[2:]
    # get only the cells we want out of the row (columns 1,2,3,5)
    for tr in rows:
        td = []
        for j in [0, 1, 2, 4]:
            td.append(tr.find_all('td')[j])
        strings = [i.text for i in td]
        cells = strings
        pet_list.append(cells)
    context = {'pet_list': pet_list}
    print(pet_list)
    return render(request, 'PetAdoption/PetAdoption_statistics.html', context)


# Petfinder API request functions:

def get_access_token():
    # from petfinder api documentation, converted curl commands to python
    data = {
        'grant_type': 'client_credentials',
        'client_id': '7hE0KUXcBfMv65qj5sHjVzXSpzfH949wkefITm6y49nupe0NZA',
        'client_secret': '8y8tAJxIL8sZLkCf7KvTZx8OYCnSWbvYKt5WBwg5'
    }

    response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
    # from the response get just the access token
    token_response = json.loads(response.text)
    my_access_token = token_response['access_token']

    return my_access_token


def pet_adoption_portland(request):
    species = ' '
    animals_avail = {}

    if 'species' in request.POST:
        # take user input of species
        species = request.POST['species']

        # get the access token by calling the get_access_token function from above
        access_token = get_access_token()

        # the request based on Petfinder's API documentation, converted from curl commands
        headers = {
            'Authorization': 'Bearer ' + access_token,
        }

        # the search parameters we want (chosen from Petfinder's API documentation) + user input
        params = (
            ('type', species),
            ('location', 'Portland, Oregon'),
            ('limit', '6'),
        )

        response = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
        animals_avail = json.loads(response.text)

    context = animals_avail
    print(context)
    return render(request, 'PetAdoption/PetAdoption_portland.html', context)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('https://api.petfinder.com/v2/{CATEGORY}/{ACTION}?{parameter_1}={value_1}',
    # headers=headers)


def pet_adoption_add(request, animal):
    form = PetForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pet_adoption_all')
    context = {'form': form, 'animal': animal}
    return render(request, 'PetAdoption/PetAdoption_add.html', context)

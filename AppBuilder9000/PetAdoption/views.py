from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from .forms import PetForm
import requests
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



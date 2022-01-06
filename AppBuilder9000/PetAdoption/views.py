from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from .forms import PetForm


def pet_adoption_home(request):
    return render(request, 'PetAdoption/PetAdoption_home.html')


def pet_adoption_list(request):
    form = PetForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pet_adoption_home')
    content = {'form': form}
    return render(request, 'PetAdoption/PetAdoption_list.html', content)


def pet_adoption_dogs(request):
    dogs = Pet.Pets.all().filter(species='Dog')
    content = {'dogs': dogs}
    return render(request, 'PetAdoption/PetAdoption_dogs.html', content)


def pet_adoption_cats(request):
    cats = Pet.Pets.all().filter(species='Cat')
    content = {'cats': cats}
    return render(request, 'PetAdoption/PetAdoption_cats.html', content)


def pet_adoption_other(request):
    others = Pet.Pets.all().filter(species='Other')
    content = {'others': others}
    return render(request, 'PetAdoption/PetAdoption_other.html', content)


def pet_adoption_all(request):
    pets = Pet.Pets.all()
    content = {'pets': pets}
    return render(request, 'PetAdoption/PetAdoption_all.html', content)

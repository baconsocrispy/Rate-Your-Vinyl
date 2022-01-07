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


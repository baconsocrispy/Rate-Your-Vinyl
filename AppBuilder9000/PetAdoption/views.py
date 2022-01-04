from django.shortcuts import render, redirect
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


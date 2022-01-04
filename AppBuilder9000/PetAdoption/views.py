from django.shortcuts import render


def pet_adoption_home(request):
    return render(request, 'PetAdoption/PetAdoption_home.html')




from django.shortcuts import render, redirect
from .models import Ryder
from .forms import RyderForm


def home(request):
    return render(request, "SnowboardingHome.html")

def AddNewRyder(request):
    form = RyderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('AddNewRyder')
    content = {'form': form}
    return render(request, 'New_Ryder.html', content)

def GetAllRyders(request):
    if request.method == 'GET':
        ryders_queryset = Ryder.objects.all() #returns queryset
        ryders_dict = {'ryders': ryders_queryset}
        return render(request, 'Dear_Ryder.html', ryders_dict)
        # get functions must return a dictionary not a queryset


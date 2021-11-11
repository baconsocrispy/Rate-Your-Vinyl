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


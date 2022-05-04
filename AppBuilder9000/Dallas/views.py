from django.shortcuts import render, redirect
from .forms import DallasForm
from .models import Dallas

def home(request):
    return render(request, 'Dallas/Dallas_home.html')

def raffle(request):
    form = DallasForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'Dallas/Dallas_raffle.html', context)
from django.shortcuts import render, redirect
from .forms import DestinationForm

def home(request):
    return render(request, 'TravelDestinations/TravelDestinations_home.html')

def TravelDestinations_add(request):
    form = DestinationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('TravelDestinations_add.html')
    content = {'form': form}
    return render(request, 'TravelDestinations/TravelDestinations_add.html', content)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurants
from .forms import RestaurantForm

def home(request):
    return render(request, 'NYC_Guide/nyc_home.html')

def add_rest(request):
    form= RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('nyc_guide_home')
    content = {'form': form}
    return render(request, 'NYC_Guide/add_rest.html', content)

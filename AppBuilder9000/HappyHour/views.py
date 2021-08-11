from django.http import HttpResponse
from django.shortcuts import render
from .forms import RestaurantsForm

def home(request):
    return render(request, 'HappyHour/HH_Home.html')


def create_review(request):
    form= RestaurantsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'HappyHour/HH_Create_Review.html', {'form': form})


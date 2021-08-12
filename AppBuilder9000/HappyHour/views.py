from django.shortcuts import render, redirect
from .forms import RestaurantsForm
from .models import Restaurants


def home(request):
    return render(request, 'HappyHour/HH_Home.html')


def create_review(request):
    form = RestaurantsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('HH_Create_Review')
    return render(request, 'HappyHour/HH_Create_Review.html', {'form': form})

def list_review(request):
    restaurants= Restaurants.objects.all()
    return render(request, "HappyHour/HH_List.html", {'restaurants': restaurants})

def review_details(request, pk):
    details = Restaurants.objects.get(pk=pk)
    context = {'details': details}
    return render(request, "HappyHour/HH_Details.html", context)


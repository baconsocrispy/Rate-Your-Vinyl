from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, "HappyHour/HH_Details.html", {'details': details})

def review_delete(request, pk):
    item = get_object_or_404(Restaurants, pk=pk)
    form = RestaurantsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('HH_List')
    return render(request, 'HappyHour/HH_Delete.html', {'item': item, 'form': form})

def review_edit(request, pk):
    item = get_object_or_404(Restaurants, pk=pk)
    form = RestaurantsForm(data=request.POST or None, instance=item)  # selects an instance
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('HH_List')
    content = {'form': form}
    return render(request, 'HappyHour/HH_edit.html', content)
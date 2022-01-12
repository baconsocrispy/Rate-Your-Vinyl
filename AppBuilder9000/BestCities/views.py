from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlacesForm
from .models import Places

def Best_Cities_home(request): #function to render the home page
    return render(request, 'BestCities/Best_Cities_home.html')

def Best_Cities_create(request): #function to add a city to the database
    form = PlacesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Best_Cities_home')
    else:
        print(form.errors)
        form = PlacesForm()
    context = {
        'form': form,
    }
    return render(request, 'BestCities/Best_Cities_create.html', context)

def Best_Cities_topcities(request):
    topC = Places.objects.all()
    return render(request, 'BestCities/Best_Cities_topcities.html', {'topC': topC})

def Best_Cities_details(request, pk):
    item = get_object_or_404(Places, pk=pk)
    return render(request, 'BestCities/Best_Cities_details.html', {'item': item})
from django.shortcuts import render, redirect
from .models import ResortListings, ResortTraveler
from .forms import ResortListings



# Create your views here.
def resorts_home(request):
    return render(request, 'All_Inclusive_Resorts/resorts_home.html')

# Story #2: Create your model ------------------------------------------------------------------------------------------

def resorts_create(request):
    form =  ResortListings(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('')
    content = {'form': form}
    return render(request, 'All-Inclusive_Resorts/resorts_create.html', content)

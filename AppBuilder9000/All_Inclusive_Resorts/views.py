from django.shortcuts import render
from .models import ResortListings, ResortTraveler


# Create your views here.
def resorts_home(request):
    return render(request, 'All_Inclusive_Resorts/resorts_home.html')
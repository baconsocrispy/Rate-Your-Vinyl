from django.shortcuts import render

def home(request):
    return render(request, 'TravelDestinations/TravelDestinations_home.html')

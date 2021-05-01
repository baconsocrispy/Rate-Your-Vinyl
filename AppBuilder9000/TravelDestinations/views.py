from django.shortcuts import render

# Create your views here.
def TravelDestinationshome(request):
    context = {}
    return render(request, 'TravelDestinations/TravelDestinations_home.html', context)
from django.shortcuts import render

# Create your views here.

def SuperCarsHome(request):
    return render(request, 'SuperCars/Super_Cars_Home.html')
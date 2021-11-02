from django.shortcuts import render

# Create your views here.

def SportsCars_Home(request):
    return render(request, 'SportsCars_Home.html')

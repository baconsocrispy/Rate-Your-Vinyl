from django.shortcuts import render

def Sneakers_home(request):
    return render(request, "Sneakers/Sneakers_home.html")
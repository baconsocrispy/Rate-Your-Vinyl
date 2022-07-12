from django.shortcuts import render


# Create your views here.

# Story #1: Build the basic app

def marvel_home(request):
    return render(request, "Marvel/marvel_home.html")

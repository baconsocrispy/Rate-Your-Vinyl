from django.http import HttpResponse
from django.shortcuts import render

def Personality_home(request):
    return render(request, 'Personality/Personality_home.html')
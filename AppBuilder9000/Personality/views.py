from django.http import HttpResponse
from django.shortcuts import render


def personality_home(request):
    return render(request, 'Personality/personality_home.html')

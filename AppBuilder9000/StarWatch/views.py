from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def StarWatch_home(request):
    return render(request, 'StarWatch/StarWatch_home.html')

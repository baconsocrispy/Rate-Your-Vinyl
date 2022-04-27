from django.http import HttpResponse
from django.shortcuts import render


def seattle_home(request):
    return render(request, 'Seattle/seattle_home.html')

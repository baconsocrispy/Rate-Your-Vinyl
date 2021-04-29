from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def MarketWatch_home(request):
    context = {}
    return render(request, 'Resellers_MarketWatch/MarketWatch_home.html', context)
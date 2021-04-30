from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'Resellers_MarketWatch/MarketWatch_home.html')


def account(request):
    return render(request, 'Resellers_MarketWatch/AccountPage.html')


def news(request):
    return render(request, 'Resellers_MarketWatch/News.html')


def about(request):
    return render(request, 'Resellers_MarketWatch/About.html')


def register(request):
    return render(request, 'Resellers_MarketWatch/Register.html')
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'Resellers_MarketWatch/MarketWatch_home.html')


def account(request):
    return render(request, 'Resellers_MarketWatch/AccountPage.html')


def register(request):
    return render(request, 'Resellers_MarketWatch/Register.html')
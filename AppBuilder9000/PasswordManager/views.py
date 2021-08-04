from django.shortcuts import render


def PM_home(request): # renders the 'home page' @ templates/PasswordManager_home.html
    return render(request, 'PasswordManager_home.html')

# Create your views here.

from django.shortcuts import render


def PM_home(request): # renders the 'home page' @ templates/PM_home.html
    return render(request, 'PasswordManager/PM_home.html')

# Create your views here.

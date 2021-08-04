from django.shortcuts import render


# Create your views here:
def home(request): # renders the 'home page' @ templates/PasswordManager_home.html
    return render(request, 'PasswordManager/PasswordManager_home.html')


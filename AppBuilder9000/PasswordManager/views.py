from django.shortcuts import render


# Create your views here:
def home(request): # renders the 'home page' @ templates/PwdMgr_home.html
    return render(request, 'PasswordManager/PwdMgr_home.html')


def generator(request):
    return render(request, 'PasswordManager/PwdMgr_generator.html')


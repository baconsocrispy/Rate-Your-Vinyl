from django.shortcuts import render


def IceHockey_home(request):
    return render(request, 'IceHockey/IceHockey_home.html')


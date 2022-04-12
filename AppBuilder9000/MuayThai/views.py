from django.shortcuts import render


def Muay_Thai_Home(request):
    return render(request, 'MuayThai/MuayThai_Home.html')

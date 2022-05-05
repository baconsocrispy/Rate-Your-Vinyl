from django.shortcuts import render

def SLS_home(request):
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_home.html')
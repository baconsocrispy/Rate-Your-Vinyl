from django.shortcuts import render


def acnh_home(request):
    return render(request, 'home.html')

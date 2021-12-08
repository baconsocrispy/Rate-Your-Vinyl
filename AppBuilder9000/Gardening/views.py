from django.shortcuts import render


def gardening_home(request):
    return render(request, 'Gardening/gardening_home.html')

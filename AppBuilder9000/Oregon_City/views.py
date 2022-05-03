from django.shortcuts import render


def oregon_home(request):
    return render(request, 'Oregon_City/Oregon_home.html')

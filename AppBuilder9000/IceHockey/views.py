from django.shortcuts import render


def home(request):
    render(request, 'IceHockey_home.html')


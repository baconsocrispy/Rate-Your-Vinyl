from django.shortcuts import render


def home(request):
    return render(request, 'swu_home.html')


def sources(request):
    return render(request, 'swu_sources.html')


def characters(request):
    return render(request, 'swu_characters.html')

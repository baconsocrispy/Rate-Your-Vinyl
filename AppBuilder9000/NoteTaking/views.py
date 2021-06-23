from django.shortcuts import render


def home(request):
    return render(request, 'NoteTaking/NoteTaking_home.html')

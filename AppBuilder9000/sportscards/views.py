from django.http import HttpResponse
from django.shortcuts import render
from .models import Card


def home(request):
    types = ["Baseball", "Basketball", "Hockey", "Football"]
    context = {
        'types': types,
    }
    return render(request, "sportscards/sportscards_home.html", context)

def join(request):
    return render(request, 'sportscards/join.html', {})
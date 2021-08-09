from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    types = ["Baseball", "Basketball", "Hockey", "Football"]
    context = {
        'types': types,
    }
    return render(request, "homesportscards.html", context)
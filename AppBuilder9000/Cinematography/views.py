from django.http import HttpResponse
from django.shortcuts import render


def camIndex(request):
    return render(request, "Camera_home.html")

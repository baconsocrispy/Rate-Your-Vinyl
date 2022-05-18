from django.http import HttpResponse
from django.shortcuts import render


def camIndex(request):
    return render(request, "Camera_home.html")


def navbar(request):
    return render(request, "content/navbar.html")


def colors(request):
    return render(request, "content/colors.html")


def comp(request):
    return render(request, "content/comp.html")

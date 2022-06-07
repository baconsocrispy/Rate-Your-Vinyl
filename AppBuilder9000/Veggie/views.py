from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def veggie_home(request):
    return render(request, "Veggie_home.html")

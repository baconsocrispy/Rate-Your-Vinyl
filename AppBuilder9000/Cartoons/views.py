from django.shortcuts import render, redirect
import requests

# Create your views here.
""" HOME, CREATE SECTION """
def Cartoons(request):
    return render(request, 'Cartoons/Cartoons_home.html')
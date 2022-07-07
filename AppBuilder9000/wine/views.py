from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import requests

# Render the home page

def wine_home(request):
    return render(request, "wine/wine_home.html")

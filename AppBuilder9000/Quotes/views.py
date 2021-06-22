from django.shortcuts import render, redirect, get_object_or_404
import requests

# Create your views here.
def home(request):
    return render(request, 'Quotes/Quotes_home.html',)
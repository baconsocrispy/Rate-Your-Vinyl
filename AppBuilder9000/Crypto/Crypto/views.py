from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    crypto = "I am the crypto chart application"
    return HttpResponse(crypto)

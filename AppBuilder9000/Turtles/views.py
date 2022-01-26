from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to my page!")


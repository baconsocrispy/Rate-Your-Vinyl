from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404



def TrackApp_home(request):
    return render(request, "TrackApp_home.html")















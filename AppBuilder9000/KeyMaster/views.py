from django.shortcuts import render
from django.http import HttpResponse

def KeyMaster_home(request):
    return render(request, 'KeyMaster_home.html')

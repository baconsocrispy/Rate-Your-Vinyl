from django.shortcuts import render
from django.http import HttpResponse

def todoView(request):
    return HttpResponse('Greetings, This is TodoView.')

from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

# Create your views here.
def composers(request):
    return render(request, 'composers/composers_home.html')
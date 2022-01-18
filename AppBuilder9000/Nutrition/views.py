
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.

def nutrition_home(request):
    return render(request, 'Nutrition_home.html')



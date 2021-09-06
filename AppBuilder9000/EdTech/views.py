from django.shortcuts import render, redirect, get_object_or_404
from .forms import EdTechForm
from .models import EdTech

# Displays the Home page
def EdTech_Home(request):
    return render(request, 'EdTech/home.html')

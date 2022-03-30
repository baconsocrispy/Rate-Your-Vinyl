from django.shortcuts import render, redirect
from .forms import CartoonForm
from .models import Cartoon
import requests

# Create your views here.
""" HOME, CREATE SECTION """
def Cartoons(request):
    return render(request, 'Cartoons/Cartoons_home.html')

def CreateCartoon(request):
    form = CartoonForm(data=request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('Cartoons_home')
    context = {'form': form}
    return render(request, "Cartoons/Cartoons_create.html", context)

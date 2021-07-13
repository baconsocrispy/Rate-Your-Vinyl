from django.shortcuts import render
from .models import PreciousMetalsItem
from .forms import MetalForm


# Create your views here.

# home html

def home(request):
    return render(request, 'PreciousMetals_home.html', {})


# inventory html

def inventory(request):
    return render(request, 'PreciousMetals_inventory.html', {})

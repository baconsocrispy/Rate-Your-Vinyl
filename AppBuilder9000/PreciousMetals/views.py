from django.shortcuts import render, redirect
from .models import PreciousMetalsItem
from .forms import MetalForm


# Create your views here.

# home html

def home(request):
    return render(request, 'PreciousMetals_home.html', {})


# add inventory

def inventory(request):
    form = MetalForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PreciousMetals_inventory')
    content = {'form': form}
    return render(request, 'PreciousMetals_inventory.html', content)


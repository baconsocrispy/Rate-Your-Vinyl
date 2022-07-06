from django.shortcuts import render, redirect
from .models import Material
from .forms import MaterialForm

def inventory_home(request):
    return render(request, 'Inventory/Inventory_home.html')

def inventory_create(request):
    form = MaterialForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, 'Inventory/Inventory_create.html', content)


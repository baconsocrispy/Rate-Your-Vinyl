from django.shortcuts import render

def inventory_home(request):
    return render(request, 'Inventory/Inventory_home.html')

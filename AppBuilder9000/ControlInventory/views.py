from django.shortcuts import render

def home(request):
    return render(request, 'ControlInventory/ControlInventory_home.html')




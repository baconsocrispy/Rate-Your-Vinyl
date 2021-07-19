from django.shortcuts import render, redirect
from .forms import AccountForm, ProductForm



def home(request):
    return render(request, 'ControlInventory/ControlInventory_home.html')

def createuser(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ControlInventory_account.html')
    content = {'form': form}
    return render(request, 'ControlInventory/ControlInventory_account.html', content)

def addproduct(request):
    form = ProductForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ControlInventory/ControlInventory_addproduct.html')
    content = {'form': form}
    return render(request, 'ControlInventory/ControlInventory_addproduct.html', content)

def productinfo(request):
    return render(request, 'ControlInventory/ControlInventory_productinfo.html')
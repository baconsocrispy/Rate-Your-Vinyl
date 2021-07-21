from django.shortcuts import render, redirect
from .forms import AccountForm, ProductForm
from .models import Account, Product



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
            return redirect('ControlInventory_home.html')
    content = {'form': form}
    return render(request, 'ControlInventory/ControlInventory_addproduct.html', content)

def productinfo(request):
    display_accounts = Account.objects.all()
    display_products = Product.objects.all()
    if request.method == 'POST':
        pk = request.POST['account']
        return productinfo(request, pk)
    content = {'display_accounts': display_accounts, 'display_products': display_products}
    return render(request, 'ControlInventory/ControlInventory_productinfo.html', content)
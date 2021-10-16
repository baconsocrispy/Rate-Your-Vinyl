from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def Val_home(request):
    return render(request, 'ValItems/Val_home.html')


def AddItem(request):
    form = ItemForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print("VALID")
            form.save()
            return redirect('AddItem')
    return render(request, 'ValItems/AddItem.html', {'form': form})


def Items(request):
    return render(request, 'ValItems/Items.html')

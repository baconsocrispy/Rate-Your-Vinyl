from tkinter import Entry

from django.shortcuts import render, get_object_or_404, redirect
from .models import HardRock
from .forms import HardRockForm


# Create your views here.



def RocksHome(request):
    return render(request, 'Rock/RocksHome.html')


def HardRock_List(request):
    list = HardRock.objects.all()
    return render(request, 'Rock/HardRock_List.html', {'list':list})


def Rock_Create(request):
    form = HardRockForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('RocksHome')
    content = {'form': form}
    return render(request, 'Rock/Rock_Create.html', content)

def HardRock_Details(request):
    return render(request, 'Rock/HardRock_Details.html')

def admin_console(request):
    from AppBuilder9000 import Rock
    HardRock = Rock.objects.all()
    return render(request, 'Rock/HardRock_List.html', {'Rock': Rock})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(HardRock, pk=pk)
    form = HardRockForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'Rock/HardRock_List.html', {'form' : form})

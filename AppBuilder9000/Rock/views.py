from django.shortcuts import render, redirect
from .models import HardRock
from .forms import HardRockForm


# Create your views here.


def RocksHome(request):
    return render(request, 'Rock/RocksHome.html')


def HardRock_List(request):
    return render(request, 'Rock/HardRock_List.html')


def Rock_Create(request):
    form = HardRockForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('RocksHome')
    context = {'form': form}
    return render(request, 'Rock/Rock_Create.html', context)

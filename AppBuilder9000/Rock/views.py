from django.shortcuts import render

# Create your views here.

def RocksHome(request):
    return render(request, 'Rock/RocksHome.html')

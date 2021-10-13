from django.shortcuts import render

def Oregon_Rocks_Home(request):
    return render(request, 'OregonRocks/OregonRocksHome.html')
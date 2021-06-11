from django.shortcuts import render

def SciFihome(request):
    return render(request, 'SciFiWatchlist/SciFiWatchlist_home.html')

def AddMovies(request):
    return render(request, 'SciFiWatchlist/SciFiWatchlist_add.html')

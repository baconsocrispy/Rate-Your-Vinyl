from django.shortcuts import render, redirect
from .forms import MovieForm
def SciFihome(request):
    return render(request, 'SciFiWatchlist/SciFiWatchlist_home.html')

def AddMovies(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Add-Movies')
    return render(request, 'SciFiWatchlist/SciFiWatchlist_add.html', {'form': form})

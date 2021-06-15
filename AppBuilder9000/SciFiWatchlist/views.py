from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie


def SciFihome(request):
    return render(request, 'SciFiWatchlist/SciFiWatchlist_home.html')

def AddMovies(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Add-Movies')
    return render(request, 'SciFiWatchlist/SciFiWatchlist_add.html', {'form': form})

def ListMovies(request):
    Movies = Movie.objects.all()
    return render(request,"SciFiWatchlist/SciFiWatchlist_movielist.html", {'Movies': Movies})

def MovieDetails(request, id):
    Movies = get_object_or_404(Movie, id=id)
    return render(request, "SciFiWatchlist/SciFiWatchlist_details.html", {
        'name': Movies.FilmName,
        'year': Movies.ReleaseYear,
        'Starring': Movies.StarNames,
        'Directors': Movies.DirectorName,
        'Summary': Movies.MovieSummary,
    })

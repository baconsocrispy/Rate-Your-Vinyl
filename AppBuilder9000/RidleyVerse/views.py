from .forms import MovieForm
from .models import Movie
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect


def RidleyVersehome(request):
    return render(request, 'RidleyVerse/RidleyVerse_home.html')

def AddMovies(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Add-Movies')
    else:
        form = MovieForm()
    return render(request, 'RidleyVerse/RidleyVerse_add.html', {'form': form})

def ListMovies(request):
    Movies = Movie.objects.all().order_by("FilmName")
    return render(request,"RidleyVerse/RidleyVerse_movielist.html", {'Movies': Movies})
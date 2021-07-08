from .forms import MovieForm
from .models import Movie
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

# Nav Button functions.


def RidleyVersehome(request):
    return render(request, 'RidleyVerse/RidleyVerse_home.html')


def ListMovies(request):
    Movies = Movie.objects.all().order_by("FilmName")
    return render(request,"RidleyVerse/RidleyVerse_movielist.html", {'Movies': Movies})


def MovieDetails(request, id):
    Movies = get_object_or_404(Movie, id=id)
    return render(request, "RidleyVerse/RidleyVerse_details.html", {
        'name': Movies.FilmName,
        'year': Movies.ReleaseYear,
        'Starring': Movies.StarNames,
        'Directors': Movies.DirectorName,
        'Summary': Movies.MovieSummary,
    })
# End Nav Button functions.
# --------------------------------------------
# Modification controls


def AddMovies(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Add-Movies')
    else:
        form = MovieForm()
    return render(request, 'RidleyVerse/RidleyVerse_add.html', {'form': form})


def DeleteMovies(request, id):
    Movies = get_object_or_404(Movie, id=id)
    form = MovieForm(request.POST or None, instance=Movies)
    if request.method == "POST":
        Movies.delete()
        return HttpResponseRedirect('/RidleyVerse/List-Movies/')
    return render(request, "RidleyVerse/RidleyVerse_Delete.html", {"form": form })


def EditMovies(request, id):
    Movies = get_object_or_404(Movie, id=id) # This sets the movie id base on what was chosen by the user.
    form = MovieForm(request.POST or None, instance=Movies)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect( '/RidleyVerse/'+ id)
    return render(request, "RidleyVerse/RidleyVerse_Update.html", {"form": form })
# End Modification controls

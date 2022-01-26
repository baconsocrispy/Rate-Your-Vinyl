from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import MovieForm
from .models import Movies


# Create your views here.
def homepage(request):
    return render(request, 'MovieReviews/moviereviews_home.html')


def moviereviews_create(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('moviereviews_home')

    context = {
        'form': form
    }
    return render(request, 'MovieReviews/moviereviews_create.html', context)


def moviereviews_display(request):
    movies = Movies.Movies.all()
    context = {
        'movies': movies
    }
    return render(request, 'MovieReviews/moviereviews_display.html', context)


def moviereviews_details(request, pk):
    movie_item = get_object_or_404(Movies, pk=pk)
    context = {'movie_item': movie_item
    }
    return render(request, 'MovieReviews/moviereviews_details.html', context)


def moviereviews_edit(request, pk):
     movie_item = get_object_or_404(Movies, pk=pk)
     form = MovieForm(data=request.POST or None, instance=movie_item)
     if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('moviereviews_display')
        else:
            print(form.errors)
     else:
        return render(request, 'MovieReviews/moviereviews_edit.html', {'form': form, 'movie_item': movie_item})


def moviereviews_delete(request, pk):
    movie_item = get_object_or_404(Movies, pk=pk)
    if request.method == 'POST':
        movie_item.delete()
        return redirect('moviereviews_display')
    context = {'movie_item': movie_item}
    return render(request, 'MovieReviews/moviereviews_delete.html', context)









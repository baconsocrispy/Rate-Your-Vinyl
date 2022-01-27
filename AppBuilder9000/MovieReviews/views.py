from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import MovieForm
from .models import Movies
import requests
from bs4 import BeautifulSoup


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

# Use Beautiful Soup to scrape movie data
def moviereviews_scraping(request):
    movie_list = []
    rating_list = []
    page = requests.get("https://www.imdb.com/list/ls024149810/")
    soup = BeautifulSoup(page.content, 'html.parser')
    movie = soup.find('div', class_='sub-list')
    title = movie.find_all('h3', class_='lister-item-header')
    for i in title:
        name = i.find('a')
        movie_title = name.text
        movie_list.append(movie_title)
    movie_ratings = movie.find_all('div', class_='ipl-rating-widget')
    for b in movie_ratings:
        stars = b.find('span', class_='ipl-rating-star__rating')
        rating = stars.text
        rating_list.append(rating)
    print(rating_list)
    print(movie_list)
    movie_info = zip(movie_list, rating_list)
    context = {'movie_info': movie_info}
    return render(request, 'MovieReviews/moviereviews_scraping.html', context)













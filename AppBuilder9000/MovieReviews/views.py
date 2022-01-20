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

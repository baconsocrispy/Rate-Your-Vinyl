from django.shortcuts import render, redirect, get_object_or_404
from .models import Ani
from .forms import AniForm


# Story #1: Build the basic app -----------------------------------------------------
def anime_home(request):
    return render(request, 'anime/anime_home.html')


# Story #2: Create your model ------------------------------------------------------
def create_anime(request):
    form = AniForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../anime_archive')
    context = {'form': form}
    return render(request, 'anime/create_anime.html', context)







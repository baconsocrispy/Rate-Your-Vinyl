from django.shortcuts import render, redirect
from .forms import NewAnime


def anime_reviews_home(request):
    return render(request, "anime_reviews_home.html")


def anime_reviews_create(request):
    form = NewAnime(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('anime_reviews_create')
    else:
        print(form.errors)
        form = NewAnime()
        context = {'form': form}
    return render(request, 'anime_reviews_create.html', context)

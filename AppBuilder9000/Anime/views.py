from django.shortcuts import render


def anime_home(request):
    return render(request, 'anime/anime_home.html', {})

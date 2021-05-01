from django.shortcuts import render


def videogamereviews(request):
    content = {}
    return render(request, 'VideoGameReviews/VideoGamesReviews_Home.html', content)

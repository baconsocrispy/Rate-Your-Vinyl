from django.shortcuts import render
from .models import VideoReviews
from .forms import VideoReviewsForm


def videogamereviews(request):
    content = {}
    return render(request, 'VideoGameReviews/VideoGamesReviews_Home.html', content)


def videoreviews(request):
    context = {}
    all_reviews = videoreviews().objects.all
    return render(request, 'VideoGameReviews/VideoGamesReviews_Reviews.html', {'all': all_reviews}, context)

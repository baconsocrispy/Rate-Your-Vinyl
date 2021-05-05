from django.shortcuts import render, redirect
from .models import VideoReviews
from .forms import VideoReviewsForm


def videogamereviews(request):
    content = {}
    return render(request, 'VideoGameReviews/VideoGamesReviews_Home.html', content)


def videoreviews(request):
    all_reviews = VideoReviews.objects.all()
    context = {'all': all_reviews}
    return render(request, 'VideoGameReviews/VideoGamesReviews_Reviews.html', context)


def create(request):
    form = VideoReviewsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("VideoGamesReviews_Create")
    context = {"form": form}
    return render(request, "VideoGameReviews/VideoGamesReviews_Create.html", context)

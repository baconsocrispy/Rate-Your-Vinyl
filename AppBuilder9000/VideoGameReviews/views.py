from django.shortcuts import render


def VideoGameReviewsHome(request):
    return render(request, 'VideoGameReviews/VideoGamesReviews_Home.html')

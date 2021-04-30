from django.shortcuts import render


def VideoGameReviewsHome(request):
    return render(request, 'VideoGameReviews/VideoGameReviews_Home.html')

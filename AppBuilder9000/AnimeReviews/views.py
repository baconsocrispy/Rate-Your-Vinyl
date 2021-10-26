from django.shortcuts import render


def anime_reviews_home(request):
    return render(request, "anime_reviews_home.html")

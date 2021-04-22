from django.shortcuts import render
from .models import Person
from .models import Review
from .forms import ReviewForm


def AnimeHome(request):
    return render(request, 'TheAnimeApp/AnimeHome.html', )


def AnimeReviews(request):
    context = {}
    all_reviews = Review.objects.all
    return render(request, 'TheAnimeApp/AnimeReviews.html', {'all': all_reviews}, context)


def AnimeCreate(request):
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'TheAnimeApp/AnimeCreate.html')
    else:
        return render(request, 'TheAnimeApp/AnimeCreate.html')

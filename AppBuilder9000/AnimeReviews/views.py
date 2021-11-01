from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewAnime
from .models import Anime


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


def anime_reviews_view(request):
    view = Anime.objects.all()
    return render(request, 'anime_reviews_view.html', {'view': view})


def anime_reviews_details(request, pk):
    details = get_object_or_404(Anime, pk=pk)
    context = {'details': details}
    return render(request, 'anime_reviews_details.html', context)

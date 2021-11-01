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


def anime_reviews_edit(request, pk):
    item = get_object_or_404(Anime, pk=pk)
    form = NewAnime(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('anime_reviews_view')

        else:
            print(form.errors)
    else:
        return render(request, 'anime_reviews_edit.html', {'form': form, 'item': item})


def anime_reviews_delete(request, pk):
    item = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('anime_reviews_view')
    context = {'item': item}
    return render(request, 'anime_reviews_delete', context)

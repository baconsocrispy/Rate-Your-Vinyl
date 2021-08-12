from django.shortcuts import render, redirect, get_object_or_404
from .models import BoardGame
from .forms import BoardGameForm


def BoardGames_home(request):
    boardgames = BoardGame.objects.all()
    return render(request, 'BoardGames/home.html', {'boardGames': boardgames})


def BoardGames_get(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    return render(request, 'BoardGames/get.html', {'boardgame': boardgame})


def BoardGames_create(request):
    form = BoardGameForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('BoardGames_create')
    else:
        return render(request, 'BoardGames/create.html', {'form': form})


def BoardGames_insert(request):
    form = BoardGameForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    content = {'form': form}
    return render(request, 'BoardGames/get.html', content)

from django.shortcuts import render, redirect, get_object_or_404
from .models import BoardGame
from .forms import BoardGameForm


def BoardGames_home(request):
    return render(request, 'BoardGames/home.html')


def BoardGames_games(request):
    return render(request, 'BoardGames/games.html')


def BoardGames_game(request, pk):
    content = get_object_or_404(BoardGame, pk=pk)
    return render(request, 'BoardGames/details.html', content)


def BoardGames_create(request):
    form = BoardGameForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('entryCreated.html')
    content = {'form': form}
    return render(request, 'BoardGames/newGameEntry.html', content)


def BoardGames_insertGame(request):
    form = BoardGameForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    content = {'form': form}
    return render(request, 'BoardGames/entryCreated.html', content)

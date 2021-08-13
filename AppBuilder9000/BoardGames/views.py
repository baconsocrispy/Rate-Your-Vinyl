from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BoardGame
from .forms import BoardGameForm


def BoardGames_home(request):
    return render(request, 'BoardGames/home.html')


def BoardGames_get(request, pk):
    content = get_object_or_404(BoardGame, pk=pk)
    return render(request, 'BoardGames/details.html', content)


def BoardGames_edit(request, pk):
    return render(request, 'BoardGames/edit.html', {'boardgame': BoardGame.objects.get(id=pk)})


def BoardGames_create(request):
    form = BoardGameForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            record = form.save()
            return redirect('BoardGames_get', pk=record.id)
    else:
        content = {'form': form}
        return render(request, 'BoardGames/.html', content)
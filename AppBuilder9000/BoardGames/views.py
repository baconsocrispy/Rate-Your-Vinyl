from django.shortcuts import render, redirect, get_object_or_404
from .models import BoardGame
from .forms import BoardGameForm
#import requests
#import xml.etree.ElementTree as ET


def BoardGames_home(request):
    boardgames = BoardGame.objects.all()
    return render(request, 'BoardGames/home.html', {'boardGames': boardgames})


def BoardGames_get(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    return render(request, 'BoardGames/get.html', {'b': boardgame})


def BoardGames_create(request):
    form = BoardGameForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('BoardGames_get', pk=result.id)
    else:
        return render(request, 'BoardGames/create.html', {'form': form})


def BoardGames_edit(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    form = BoardGameForm(request.POST or None, instance=boardgame)
    if request.POST and form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return render(request, 'Boardgames/get.html', {'b': boardgame})
    else:
        context = {'form': form,
                   'id': boardgame.pk,
                   'error': 'The form was not updated successfully. Please enter valid information.'}
        return render(request, 'BoardGames/edit.html', context)

def BoardGames_delete(request, pk):
    BoardGame.objects.filter(id=pk).delete()
    boardgames = BoardGame.objects.all()
    return render(request, 'BoardGames/home.html', {'boardGames': boardgames})

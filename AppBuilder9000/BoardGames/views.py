from html import unescape
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import BoardGame
from .forms import BoardGameForm


def BoardGames_home(request):
    boardgames = BoardGame.objects.all()
    return render(request, 'BoardGames/home.html', {'boardGames': boardgames})


def BoardGames_get(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    boardgame.Description = unescape(boardgame.Description)
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


def BoardGames_favorite(request, pk):
    #print("Test")
    #content = json.dumps(boardgame)
    #print(content)
    ##return render(json.dumps(content))
    if request.method == "POST":
        pk = request.POST.get("id")
        boardgame = BoardGame.objects.get(id=pk)
        boardgame.Favorite = not boardgame.Favorite
        boardgame.save()
        print(request.POST)
        data = { "msg": "Favorite toggled.", 'value': boardgame.Favorite, 'id': pk, }
        return JsonResponse(data)
    else:
        data = { "msg": "Message received!", 'value': boardgame.Favorite, 'id': pk, }


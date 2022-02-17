from django.shortcuts import render, redirect, get_object_or_404
from .forms import GamesForm
from .models import Games


def homepage(request, pk=0):
    return render(request, 'ChessOpenings/chess_index.html')


def add_game(request):
    form = GamesForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            test = form.save()
            print(test.title)
            return redirect(homepage)
    return render(request, "ChessOpenings/add_game.html", context)


# Create your views here.
def search_games(request):
    all_entries = Games.Game.all()
    print(all_entries)
    context = {'games': all_entries}
    return render(request, "ChessOpenings/chess_search.html", context)


# Create your views here.
def game_details(request, pk):
    details = get_object_or_404(Games, pk=pk)
    context = {'game': details}
    return render(request, "ChessOpenings/game_details.html", context)

def game_edit(request, pk):
    details = get_object_or_404(Games, pk=pk)
    context = {'game': details}
    return render(request, "ChessOpenings/edit", context)



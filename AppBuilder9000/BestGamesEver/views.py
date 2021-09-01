from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game

# Displays the home page
def BestGamesEver_Home(request):
    return render(request, 'BestGamesEver/home.html')

def Game_Create(request):
    form = GameForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect("Game_Create")

    return render(request, 'BestGamesEver/Gamecreate.html', {"form": form})

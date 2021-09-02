from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game

# Displays the home page
def BestGamesEver_Home(request):
    return render(request, 'BestGamesEver/home.html')

#Function for user to create a Db entry
def Game_Create(request):
    form = GameForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect("Game_Create")

    return render(request, 'BestGamesEver/Gamecreate.html', {"form": form})

# Function to retrieve all items from our Db
def Game_View(request):
    #gets all objects of the Game database unsorted
    game_list = Game.objects.all()

    return render(request, 'BestGamesEver/ViewGames.html', {'game_list': game_list})

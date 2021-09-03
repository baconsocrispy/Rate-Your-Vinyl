from django.shortcuts import render, redirect, get_object_or_404
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


# Function to allow user to view a single item

def Game_Details(request, game_id):
    details = Game.objects.get(id=game_id)
    return render(request, "BestGamesEver/Game_Details.html", {'details': details})

# Function to edit an entry

def Edit_Games(request, game_id):
    item = get_object_or_404(Game, id=game_id)
    form = GameForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("Game_View")
    content = {'form': form}
    return render(request, 'BestGamesEver/Game_Edit.html', content)


# Function to delete an entry
def Delete_Games(request, game_id):
    item = get_object_or_404(Game, id=game_id)
    form = GameForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
            item.delete()
            return redirect("Game_View")
    content = {'form': form}
    return render(request, 'BestGamesEver/Game_Delete.html', {'item': item, 'form': form})


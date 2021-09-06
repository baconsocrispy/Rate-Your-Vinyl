from django.shortcuts import render, redirect, get_object_or_404
from .forms import GameForm
from .models import Game
from bs4 import BeautifulSoup
import requests





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






def View_Price(request, game_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

    }
    r = requests.get("https://store.steampowered.com/app/291650/Pillars_of_Eternity/")
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.select_one(selector=".apphub_AppName").getText()

    price = soup.select_one(selector=".game_purchase_action_bg").getText()
    price = price.strip()
    price = price[1:]
    para_text = parseSoup()
    context = {'para_text': para_text}
    return render (request, 'BestGamesEver/View_Price.html', context)



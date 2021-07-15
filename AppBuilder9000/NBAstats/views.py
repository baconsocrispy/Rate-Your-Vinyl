from django.shortcuts import render, redirect, get_object_or_404
from .models import Defensive_Stats
from .forms import Def_Stats_Form
from bs4 import BeautifulSoup
import requests


# RENDER HOME PAGE
def nba_home(request):
    form = Def_Stats_Form(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('stats-home')
    content = {'form': form}
    return render(request, 'nba-home.html', content)


# ===============================================================================================
#       Display functions to show All players, or players from specific seasons (i.e. 2020-2021)
# ===============================================================================================
def display_all(request):
    players = Defensive_Stats.objects.all()
    content = {'players': players}
    return render(request, 'nba-display.html', content)


def display_2021(request):
    year = '2020-2021'
    # Here we use Raw SQL commands to only show records from chosen year
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2020-2021.html', content)


def display_2020(request):
    year = '2019-2020'
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2019-2020.html', content)


def display_2019(request):
    year = '2018-2019'
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2018-2019.html', content)


# ===============================================================================================
#           Display the details for individual players
# ===============================================================================================
def show_details(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    year = player.year
    name = player.playerName
    rebs = player.defRebs
    steals = player.steals
    blocks = player.blocks

    # Total Points are calculated below
    total_def_points = rebs + (steals * 3) + (blocks * 3)

    content = {'player': player,
               'year': year,
               'playerName': name,
               'defRebs': rebs,
               'steals': steals,
               'blocks': blocks,
               'total_def_points': total_def_points,
               }
    return render(request, 'nba-details.html', content)


# ===============================================================================================
#           EDIT and DELETE player functions
# ===============================================================================================
def delete_player(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    year = player.year
    form = Def_Stats_Form(data=request.POST or None, instance=player)
    if request.method == 'POST':
        player.delete()
        return redirect('display-all')
    content = {'player': player, 'year': year, 'form': form}
    return render(request, 'nba-delete.html', content)


def edit_player(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    form = Def_Stats_Form(data=request.POST or None, instance=player)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('display-all')
    content = {'form': form}
    return render(request, 'nba-edit.html', content)


# ===============================================================================================
#           Beautiful Soup
# ===============================================================================================
def b_ref(request):
    # NBA season we will be analyzing
    year = 2021
    # URL page we will scraping (see image above)
    brURL = "https://www.basketball-reference.com/leagues/NBA_2021_totals.html"
    # this is the HTML from the given URL
    page = requests.get(brURL)
    # print(page.status_code) # Print status code to terminal - 200 means no errors
    soup = BeautifulSoup(page.content, 'html.parser')
    # print([type(item) for item in list(soup.children)])

    # Get all Headers from table and put them in a list
    headers = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    # Select only the headers I want and put them in a list
    myHeaders = list(headers[i] for i in [1,4,22,25,26])
    print(myHeaders)

    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    print(player_stats)

    return render(request, 'nba-basketball-reference.html')
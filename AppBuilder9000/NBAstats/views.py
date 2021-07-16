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
    # URL page we will scraping
    brURL = "https://www.basketball-reference.com/leagues/NBA_2021_totals.html"

    page = requests.get(brURL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print([type(item) for item in list(soup.children)])

    # Get all Headers from table and put them in a list
    headers = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    # Select only the headers I want and put them in a list
    myHeaders = list(headers[i] for i in [1, 22, 25, 26])
    print(myHeaders)  # This shows which headers I've selected

    # Get all table rows (tr) and put into a list.
    # Omitted row with index 0 and started at index 1 (that's what [1:] does).
    rows = soup.findAll('tr')[1:]
    # Extract table data (td) from the rows and put into list
    allStats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

    # This print shows how we can select just the first element (name [0]) in the second row [1]
    print(allStats[1][0])
    # I could print all the players and all their stats with print(allStats)
    # But that is a lot to print to console (over 500 rows)

    ''' Here I declare a dictionary myStats, iterate through the stats I've scraped,
        declare an instance of my model, and attempt to add each player with specific
        stats to the dictionary. It does in fact create a dictionary, but I don't know
        if the model is actually doing anything, and each iteration overwrites the 
        previous dictionary because of like key names.
    '''
    myStats = {}
    i = 0
    while i < 10:  # I only iterate 10 times so it doesn't go all the way through the entire data set
        p = Defensive_Stats()
        p.playerName = {'playerName': list(allStats[i][0:1])}
        p.defRebs = {'defRebs': list(allStats[i][21:22])}
        p.steals = {'steals': list(allStats[i][24:25])}
        p.blocks = {'blocks': list(allStats[i][25:26])}

        myStats.update(p.playerName)
        myStats.update(p.defRebs)
        myStats.update(p.steals)
        myStats.update(p.blocks)
        i += 1
        # Now I can print each player and the associated stats I have chosen
        print(myStats)

    return render(request, 'nba-basketball-reference.html', myStats)

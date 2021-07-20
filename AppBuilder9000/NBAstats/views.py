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
    # URL page we will scrape
    brURL = "https://www.basketball-reference.com/leagues/NBA_2021_totals.html"

    page = requests.get(brURL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print([type(item) for item in list(soup.children)])

    # Get all Headers from table and put them in a list
    headers = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    # Select only the headers I want and put them in a list
    myHeaders = list(headers[i] for i in [1, 22, 25, 26])
    # print(myHeaders)  # This shows which headers I've selected

    # Get all table rows (tr) and put into a list.
    # Omitted row with index 0 and started at index 1 through 20
    rows = soup.findAll('tr')[1:20]
    # Extract table data (td) from the rows and put into list
    allStats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]
    # This print shows how we can select just the first element (name [0]) in the second row [1]
    # print(allStats[0][0])
    # I could print all the players and all their stats with print(allStats)
    # But that is a lot to print to console (over 500 rows)
    statsList = []
    myStats = {}
    player_dict = {}
    check_name = ''
    i = 0
    while i < len(allStats):  # I only iterate 10 times so it doesn't go all the way through the entire data set
        ''' Get data from allStats, which comes out as a list'''
        playerNameValue = allStats[i][0]
        defRebsValue = allStats[i][21]
        stealsValue = allStats[i][24]
        blocksValue = allStats[i][25]

        ''' Take data from lists above and convert to type int (except for name) '''
        playerName = playerNameValue
        defRebs = int(defRebsValue)
        steals = int(stealsValue)
        blocks = int(blocksValue)

        # The page I'm scraping has multiple rows for a player who changed teams
        # during the season, so this if statement checks to see if I have already
        # gotten the player's total stats
        if playerName != check_name:
            keyNum = str(i)
            # statsList = [playerName, defRebs, steals, blocks]
            # dict_item = {'key{}'.format(keyNum): statsList}
            myStats = {'playerName': playerName, 'defRebs': defRebs, 'steals': steals, 'blocks': blocks}
            dict_item = {'key{}'.format(keyNum): myStats}
            player_dict.update(dict_item)
            i += 1

        else:
            i += 1

        check_name = playerName
    print(player_dict)
    return render(request, 'nba-basketball-reference.html', player_dict)
